from django.db import models

# Create your models here.

class Todo(models.Model):
    # id = models.AutoField(primary_key=True,auto_created=True,default=0, serialize=True)
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title