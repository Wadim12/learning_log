from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import TopicForm, EntryForm
from .models import Topic, Entry

def home(request):
    return render(request, "learning_logs/home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Аккаунт создан. Добро пожаловать!")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def dashboard(request):
    topics = Topic.objects.filter(owner=request.user).annotate(entry_count=Count("entries"))
    total_entries = Entry.objects.filter(topic__owner=request.user).count()
    return render(request, "learning_logs/dashboard.html", {
        "topics": topics[:6], "topic_count": topics.count(), "entry_count": total_entries,
    })

@login_required
def topic_list(request):
    query = request.GET.get("q", "").strip()
    topics = Topic.objects.filter(owner=request.user).annotate(entry_count=Count("entries"))
    if query:
        topics = topics.filter(text__icontains=query)
    return render(request, "learning_logs/topic_list.html", {"topics": topics, "query": query})

@login_required
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk, owner=request.user)
    return render(request, "learning_logs/topic_detail.html", {"topic": topic})

@login_required
def topic_create(request):
    form = TopicForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        topic = form.save(commit=False)
        topic.owner = request.user
        topic.save()
        messages.success(request, "Тема добавлена!")
        return redirect("topic_detail", pk=topic.pk)
    return render(request, "learning_logs/form.html", {"form": form, "title": "Новая тема", "button": "Создать тему"})

@login_required
def topic_edit(request, pk):
    topic = get_object_or_404(Topic, pk=pk, owner=request.user)
    form = TopicForm(request.POST or None, instance=topic)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Изменения сохранены.")
        return redirect("topic_detail", pk=pk)
    return render(request, "learning_logs/form.html", {"form": form, "title": "Редактировать тему", "button": "Сохранить"})

@login_required
@require_POST
def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk, owner=request.user)
    topic.delete()
    messages.success(request, "Тема удалена.")
    return redirect("topic_list")

@login_required
def entry_create(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk, owner=request.user)
    form = EntryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        entry = form.save(commit=False)
        entry.topic = topic
        entry.save()
        messages.success(request, "Запись сохранена.")
        return redirect("topic_detail", pk=topic.pk)
    return render(request, "learning_logs/form.html", {"form": form, "title": "Новая запись", "button": "Сохранить запись", "topic": topic})

@login_required
def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk, topic__owner=request.user)
    form = EntryForm(request.POST or None, instance=entry)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Запись обновлена.")
        return redirect("topic_detail", pk=entry.topic_id)
    return render(request, "learning_logs/form.html", {"form": form, "title": "Редактировать запись", "button": "Сохранить", "topic": entry.topic})

@login_required
@require_POST
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, topic__owner=request.user)
    topic_pk = entry.topic_id
    entry.delete()
    messages.success(request, "Запись удалена.")
    return redirect("topic_detail", pk=topic_pk)
