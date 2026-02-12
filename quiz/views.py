from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
import json
from .models import (
     Home,ScratcLesson,ScratchCourse,LessonContent,
     Fact,AllScratchFacts,QuizLevel
     )
from .form import RegisterForm
# Create your views here.



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Գրանցումը հաջողությամբ կատարվեց։")
            return redirect("login")  # կամ "home"
    else:
        form = RegisterForm()

    return render(request, "quiz/register.html", {"form": form})



def index(request):
    home = Home.objects.first()
    return render(request, "quiz/index.html",{'home': home})


def lesson(request):
    less = ScratcLesson.objects.first()
    course = ScratchCourse.objects.all()
    lessonContent = LessonContent.objects.all()

    lessons_dict = {}
    for l in lessonContent:
        lessons_dict[str(l.id)] = {
            'title': l.title,
            'content': l.content,
            'quiz': l.quiz
        }

    return render(request, "quiz/lessons.html", {
        "less": less,
        "course": course,
        "lessonContent": lessons_dict,  
    })



def fact(request):
    fact = Fact.objects.first()

    allScratchFacts_qs = AllScratchFacts.objects.all()

    allScratchFacts = []
    for f in allScratchFacts_qs:
        allScratchFacts.append({
            "id": f.id,
            "title": f.title,
            "text": f.text,
        })

    return render(request, "quiz/fact.html", {
        "fact": fact,
        "allScratchFacts": allScratchFacts, 
    })


def quizes(request):
    quiz = {
        "heading": "Scratch Quizes",
        "title": ">Մտքի Բլոկ",
        "descrption": "Մենք օգնում ենք երեխաներին և սկսնակներին բացահայտել իրենց երևակայությունը, սովորել մտածել ճիշտ և ստեղծել ուրախ խաղեր ու անիմացիաներ, աջակցում ենք ՝ զարգացնելու իրենց երևակայությունը, մտածողությունը և ինքնավստահությունը՝ Scratch-ում ստեղծելով խաղեր և անիմացիաներ"
    }
    quizData = {}

    levels = QuizLevel.objects.prefetch_related("questions")

    for level in levels:
            quizData[level.name] = []

            for q in level.questions.all():
                quizData[level.name].append({
                    "q": q.question,
                    "options": [q.option1, q.option2, q.option3],
                    "answer": q.correct_answer,
                    "hint": q.hint
                })
    return render(request, "quiz/quizes.html", {'quizData': quizData, 'quiz': quiz})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Էլ․ հասցե կամ գաղտնաբառ սխալ է։")
            return redirect("login")

        user = authenticate(username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Էլ․ հասցե կամ գաղտնաբառ սխալ է։")
            return redirect("login")

    return render(request, "quiz/login.html")

