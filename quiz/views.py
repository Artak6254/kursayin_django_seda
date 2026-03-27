from django.shortcuts import render
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder

from .models import (
     Home,ScratcLesson,ScratchCourse,LessonContent,
     Fact,AllScratchFacts,QuizLevel
     )
from .form import RegisterForm
# Create your views here.




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





def contact(request):
    contact = {
        "heading": "Կապ մեզ հետ",
        "descr": "Ուղարկիր մեզ հաղորդագրություն, և մենք կպատասխանենք հնարավորինս շուտ։",
        "contact_btn": "ՈւՂԱՐԿԵԼ ՆԱՄԱԿ"
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
Անուն: {name}
Email: {email}

Հաղորդագրություն:
{message}
"""

        send_mail(
            subject="Նոր հաղորդագրություն",
            message=full_message,
            from_email="poghos877@gmail.com",
            recipient_list=[email],
        )

        return  render(request, "quiz/sendcontact.html")

    return render(request, "quiz/contact.html", {'contact': contact})



