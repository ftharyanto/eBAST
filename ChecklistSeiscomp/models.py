from django.db import models

# Create your models here.

# declare a new model with a name "GeeksModel"
class ChecklistSeiscompModel(models.Model):
 
    # fields of the model
    date = models.DateField(null=True)
    gaps = models.CharField(max_length=300, null=True, blank=True)
    spikes = models.CharField(max_length=300, null=True, blank=True)
    blanks = models.CharField(max_length=300, null=True, blank=True)
    operator = models.CharField(max_length=100, null=True)
    group = models.IntegerField(null=True)
    # time = models.IntegerField(null=True, blank=True)
    
class OperatorModel(models.Model):
    name = models.CharField(max_length=100)