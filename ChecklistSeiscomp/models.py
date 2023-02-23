from django.db import models

# Create your models here.

# declare a new model with a name "GeeksModel"
class ChecklistSeiscompModel(models.Model):
 
    # fields of the model
    date = models.DateField()
    gaps = models.JSONField(null=True)
    spikes = models.JSONField(null=True)
    blanks = models.JSONField(null=True)
    operator = models.CharField(max_length=100)
    group = models.IntegerField()
    time = models.IntegerField()
    gaps_count = models.IntegerField()
    spikes_count = models.IntegerField()
    blanks_count = models.IntegerField()
    total_count = models.IntegerField()



 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
class Operator(models.Model):
    operator = models.CharField(max_length=100)