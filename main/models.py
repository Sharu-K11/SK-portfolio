from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150 , null=False)
    description  = models.TextField()
    badges = models.CharField(max_length=100 , null= True)
    last_modified = models.DateTimeField(auto_now_add=True)
    github_link = models.URLField(max_length=200,blank=True,null=True)
    live_link = models.URLField(max_length=200,blank=True,null=True)


    @property
    def badges_list(self):
        return self.badges.split(',')

    def __str__(self):
        return f'{self.title} - {self.last_modified}'




class Email(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField()
    message = models.TextField()


    def __str__(self):
        return f"{self.name} + {self.email} "