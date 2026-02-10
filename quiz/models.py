from django.db import models

# Create your models here.
class Home(models.Model) : 
    heading = models.CharField(max_length=180)
    text = models.TextField() 
    title = models.CharField(max_length=180)
    decription = models.TextField() 
    btn_text =  models.CharField(max_length=60)

    def __str__(self):
        return self.heading
           


class ScratcLesson(models.Model):
    heading = models.CharField(max_length=255, null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title


class ScratchCourse(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    btn_text = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.title}"



class LessonContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  
    quiz = models.JSONField(default=list)

    def __str__(self):
        return self.title
    


class Fact(models.Model):
    title = models.CharField(max_length=180)
    heading = models.CharField(max_length=190)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class AllScratchFacts(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title
    


class Quiz(models.Model):
    heading = models.CharField(max_length=40)
    title = models.CharField(max_length=80)
    descrption = models.TextField()
    
    def __str__(self):
        return self.heading
    



class QuizLevel(models.Model):
    name = models.CharField(max_length=20)  # level1, level2

    def __str__(self):
        return self.name


class QuizQuestion(models.Model):
    level = models.ForeignKey(
        QuizLevel,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    correct_answer = models.IntegerField()  # 0,1,2
    hint = models.TextField()

    def __str__(self):
        return self.question[:50]

