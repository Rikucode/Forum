from django.contrib import admin
from .models import Question, Answer
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    fields = ['qTitle', 'qUser', 'qDate', 'qText']
    inlines = [AnswerInline]
    list_display = ('qTitle', 'qText', 'qDate', 'qUser', 'wasPublishedRecently', 'id')


admin.site.register(Question, QuestionAdmin)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)

admin.AdminSite.site_header = "Ура админка"