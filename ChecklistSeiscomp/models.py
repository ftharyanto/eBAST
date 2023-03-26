from django.db import models

# Create your models here.
KELOMPOK = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)

WAKTU = (
    ('12:00 WIB', '12:00 WIB'),
    ('00:00 WIB', '00:00 WIB')
)

class ChecklistSeiscompModel(models.Model):
 
    # fields of the model
    tanggal = models.TextField(null=True,)
    jam = models.CharField(max_length=20, choices=WAKTU, default='12:00 WIB')
    kelompok = models.IntegerField(choices=KELOMPOK, default=1)
    operator = models.TextField(null=True,)
    gaps = models.CharField(max_length=500, null=True, blank=True)
    spikes = models.CharField(max_length=500, null=True, blank=True)
    blanks = models.CharField(max_length=500, null=True, blank=True)
    slmon = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Kelompok {self.kelompok}"
    
class OperatorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name