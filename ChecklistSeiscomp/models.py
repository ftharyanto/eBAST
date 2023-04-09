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

class StationListModel(models.Model):
    kode = models.CharField(max_length=10)
    lokasi = models.CharField(max_length=200)
    tipe = models.CharField(max_length=50)

    def __str__(self):
        return self.kode
    
class ChecklistSeiscompModel(models.Model):
 
    # fields of the model
    tanggal = models.DateField()
    jam = models.CharField(max_length=20, choices=WAKTU, default='12:00 WIB')
    kelompok = models.IntegerField(choices=KELOMPOK, default=1)
    operator = models.TextField(null=True,)
    gaps = models.CharField(max_length=500, null=True, blank=True)
    spikes = models.CharField(max_length=500, null=True, blank=True)
    blanks = models.CharField(max_length=500, null=True, blank=True)
    slmon = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        seismograph_list = StationListModel.objects.values_list('kode', flat=True)

        def remove_accelerograph(data):
            for item in data:
                if item not in seismograph_list:
                    data.remove(item)
            return data
        
        # Modify the group field here
        if self.gaps:
            self.gaps = self.gaps.upper()
            self.gaps = remove_accelerograph(self.gaps.split())
        if self.spikes:
            self.spikes = self.spikes.upper()
            self.spikes = remove_accelerograph(self.spikes.split())
        if self.blanks:
            self.blanks = self.blanks.upper()
            self.blanks = remove_accelerograph(self.blanks.split())

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.tanggal} {self.jam}'
    
class OperatorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name