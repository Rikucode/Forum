from django.contrib import admin
from .models import Topic, Answer, Theme
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer


class TopicsInline(admin.TabularInline):
    model = Topic


class ThemeAdmin(admin.ModelAdmin):
    fields = ['themeTitle', 'themeText', 'themeDate', 'themeUser', 'is_active']
    inlines = [TopicsInline]
    list_display = ('themeTitle', 'themeText', 'themeDate', 'themeUser', 'is_active','id')
    actions = ['approve_themes']

    def approve_themes(self, request, queryset):
        queryset.update(is_active=True)


admin.site.register(Theme, ThemeAdmin)


class TopicAdmin(admin.ModelAdmin):
    fields = ['topicTitle', 'topicUser', 'topicDate', 'topicText']
    inlines = [AnswerInline]
    list_display = ('topicTitle', 'topicText', 'topicDate', 'topicUser', 'id')


admin.site.register(Topic, TopicAdmin)


class AnswerAdmin(admin.ModelAdmin):
    fields = ['answerTopic', 'answerUser', 'answerText', 'answerDate']
    list_display = ('answerTopic', 'answerUser', 'answerText', 'answerDate')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.AdminSite.site_header = "Ура админка"