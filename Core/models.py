from django.db import models

# Create your models here.
class ProjectUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=2000)
    start_date = models.DateField()
    estimate_end_date = models.DateField()
    

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_project_user = models.ManyToManyField(ProjectUser, related_name="tasks", blank=True)
    start_date = models.DateField()
    estimate_end_date = models.DateField()
    actual_end_date = models.DateField()
    
    

