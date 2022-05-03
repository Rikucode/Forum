from django.utils import timezone
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Answer
from django.urls import reverse
from django.views import generic
from .forms import LoginForm, CustomUserRegistrationForm
import random
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 5

    def get_queryset(self):
        return Question.objects.order_by('-qDate')


class TopicDetailView(generic.DetailView):
    model = Question
    modelA = Answer
    template_name = 'detail.html'
    context_object_name = 'latest_answer_list'
    # paginate_by = 10

    def get_object(self):
        question = get_object_or_404(Answer, pk=self.kwargs['pk'])
        return self.modelA.objects.filter(pk=question.pk)

    def get_queryset(self):
        return Answer.objects.filter('answerQuestion')

    # def get_context_data(self, **kwargs):
    #     context = super(TopicDetailView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


def home(request):
    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1
    return render(request, 'home.html', context={'visit_count':visit_count},)


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
            return redirect(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def create_q(request):
    return render(request,'')


# def create_a(request):
#     return render(request,'')
