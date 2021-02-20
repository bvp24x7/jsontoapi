from django.db import models

# Create your models here.
class User1(models.Model):

    id          = models.CharField(max_length=50, primary_key=True)
    real_name   = models.CharField(max_length=100)
    tz          = models.CharField(max_length=100)
    

    def __str__(self):
        return self.id

class Activity_periods(models.Model):
    
    user            = models.ForeignKey(User1 , on_delete=models.CASCADE)
    start_time      = models.DateTimeField()
    end_time        = models.DateTimeField()


   


