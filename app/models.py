from django.db import models


# Create your models here.

# class signup(models.Model):
#     username = models.CharField(max_length=20)
#     email = models.EmailField(max_length=30)
#     password = models.TextField(max_length=50)
#     password1 = models.TextField(max_length=50)

# from django.db import models
class insta(models.Model):
    instagram = models.CharField(max_length=50)
    iname = models.CharField(max_length=50)
class Tele(models.Model):
    tele = models.CharField(max_length=50)
    tname = models.CharField(max_length=50)
class yt(models.Model):
    yt = models.CharField(max_length=50)
    yname = models.CharField(max_length=50)
class myemail(models.Model):
    email = models.CharField(max_length=100)
class mycontact(models.Model):
    contact = models.CharField(max_length=14)
class myphoto(models.Model):
    photo = models.ImageField(upload_to='about_photos/', blank=True, null=True)
class myinfo(models.Model):
    info= models.TextField()
class skills(models.Model):
    skill = models.CharField(max_length=70)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    
class Standard(models.Model):
    std = models.CharField(max_length=100)

    def __str__(self):
        return self.std


class Chapter(models.Model):
    name = models.CharField(max_length=100)
    std = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='Chapters')

    def __str__(self):
        return self.name

class StudyMaterial(models.Model):
    title = models.CharField(max_length=100)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='materials')
    file = models.FileField(upload_to='materials/')

    def __str__(self):
        return self.title
    


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    que = models.CharField(max_length=10)
    time_limit = models.IntegerField(default=1)  # Time limit in minutes
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)  # Optional question image
    correct_answer = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option1_image = models.ImageField(upload_to='option_images/', blank=True, null=True)  # Optional image for option1
    option2 = models.CharField(max_length=100)
    option2_image = models.ImageField(upload_to='option_images/', blank=True, null=True)  # Optional image for option2
    option3 = models.CharField(max_length=100)
    option3_image = models.ImageField(upload_to='option_images/', blank=True, null=True)  # Optional image for option3
    option4 = models.CharField(max_length=100)
    option4_image = models.ImageField(upload_to='option_images/', blank=True, null=True)  # Optional image for option4

    def __str__(self):
        return self.text
