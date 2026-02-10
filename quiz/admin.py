from django.contrib import admin
from django import forms
from .models import (
    Home,
    ScratcLesson,ScratchCourse,LessonContent,
    Fact, AllScratchFacts,QuizLevel, QuizQuestion
)
# Register your models here.

admin.site.register(Home)

admin.site.register(ScratcLesson)
admin.site.register(ScratchCourse)
admin.site.register(LessonContent)

admin.site.register(Fact)
admin.site.register(AllScratchFacts)



class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "level", "correct_answer")
    list_filter = ("level",)
    search_fields = ("question",)

admin.site.register(QuizLevel)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
