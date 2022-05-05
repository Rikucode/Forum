from django.core.paginator import Paginator, EmptyPage
from django.utils import timezone
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Topic, Answer, Theme
from django.urls import reverse
from .forms import LoginForm, CustomUserRegistrationForm, AnswerForm, TopicForm, ThemeForm
# Create your views here.


def themes(request, page=1):
    theme_list = Theme.objects.order_by('-themeDate').filter(is_active=True)
    paginator = Paginator(theme_list, 5)
    try:
        theme_list = paginator.page(page)
    except EmptyPage:
        theme_list = paginator.page(paginator.num_pages)
    return render(request, 'themes.html', {'theme_list': theme_list})


def topics(request, pk_theme, page=1):
    theme = get_object_or_404(Theme, pk=pk_theme)
    theme_id = theme.pk
    topics_list = Topic.objects.order_by('-topicDate').filter(topicTheme=pk_theme)
    topics_count = topics_list.count()
    paginator = Paginator(topics_list, 7)
    try:
        topics_list = paginator.page(page)
    except EmptyPage:
        topics_list = paginator.page(paginator.num_pages)
    return render(request, 'topics.html', {'theme':theme, 'theme_id': theme_id, 'topics_list': topics_list, 'topics_count':topics_count})


def topic_messages(request, pk_theme, pk_topic, page=1):
    theme = get_object_or_404(Theme, pk=pk_theme)
    topic = get_object_or_404(Topic, pk=pk_topic)
    theme_id = theme.pk
    topic_id = topic.pk
    messages_list = Answer.objects.order_by('-answerDate').filter(answerTopic=pk_topic)
    messages_count = messages_list.count()
    paginator = Paginator(messages_list, 10)
    message = None
    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)
        message = answer_form.save(commit=False)
        message.answerUser = request.user
        message.answerDate = timezone.now()
        message.answerTopic = topic
        message.save()
        return redirect('forum:detail', pk_theme=pk_theme, pk_topic=pk_topic, page=1)
    else:
        answer_form = AnswerForm()

    try:
        messages_list = paginator.page(page)
    except EmptyPage:
        messages_list = paginator.page(paginator.num_pages)

    return render(request, 'detail.html', {'answer_form': answer_form, 'message': message, 'theme_id':theme_id, 'topic_id': topic_id, 'topicTitle': topic.topicTitle, 'topicDate':topic.topicDate, 'topicText':topic.topicText, 'topicUser':topic.topicUser, 'messages_list': messages_list, 'messages_count': messages_count}, )


def home(request):
    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1
    return render(request, 'home.html', context={'visit_count': visit_count},)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == 'POST':
        user_form = CustomUserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('forum:login'))
    else:
        user_form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def create_topic(request, pk_theme):
    theme = get_object_or_404(Theme, pk=pk_theme)
    theme_id = theme.pk
    if request.method == 'POST':
        topic_form = TopicForm(data=request.POST)
        topic = topic_form.save(commit=False)
        # topicCheck = Topic.objects.filter(topicTheme=theme).filter(topicTitle=topic_form.topicTitle)
        # if topicCheck:
        #     return redirect('forum:home')
        # else:
        topic.topicTheme = theme
        topic.topicUser = request.user
        topic.topicDate = timezone.now()
        topic.save()
        return redirect('forum:topic', pk_theme, 1)
    else:
        topic_form = TopicForm()
    return render(request, 'create_topic.html', {'topic_form': topic_form,'theme_id':theme_id})


def create_theme(request):
    print(request.method)
    if request.method == 'POST':
        theme_form = ThemeForm(request.POST)
        theme = theme_form.save(commit=False)
        theme.themeUser = request.user
        theme.themeDate = timezone.now()
        theme.save()
        return redirect('forum:theme', 1)
    else:
        theme_form = ThemeForm()
    return render(request, 'create_theme.html', {'theme_form': theme_form})

