from django.db import models


# Create your models here.

# class signup(models.Model):
#     username = models.CharField(max_length=20)
#     email = models.EmailField(max_length=30)
#     password = models.TextField(max_length=50)
#     password1 = models.TextField(max_length=50)

# from django.db import models
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