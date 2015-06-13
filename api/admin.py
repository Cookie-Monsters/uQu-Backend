from django.contrib import admin
from api.models import Answer, Question, User
from django import forms


class AnswerAdmin(admin.ModelAdmin):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    model = Question


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = User


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
