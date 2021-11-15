from django.db import models
from django.contrib.auth.models import User


class Fayl(models.Model):
    ad=models.CharField(max_length=264)
    muellif=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='fayllar')
    fayl=models.FileField(upload_to='documents/%Y/%m/%d',null=True, blank=True)
    aciqlama=models.TextField()

    def __str__(self):
        return str(self.ad)


class Paylas(models.Model):
    kimle=models.ForeignKey(User, on_delete=models.CASCADE, related_name='gore_bildiyi_fayllar')
    fayl=models.ForeignKey(Fayl, on_delete=models.CASCADE, related_name='paylasilan_sexsler')
    serh_yaza_biler=models.BooleanField(default=False)


    def __str__(self):
        return str(self.fayl) + ' shared with ' + str(self.kimle)
    class Meta:
        unique_together=['kimle', 'fayl']

class Serh(models.Model):
    fayl=models.ForeignKey(Fayl, on_delete=models.CASCADE, related_name='serhler')
    komment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='serh')

    def __str__(self):
        return str(self.user)+' to "'+str(self.fayl)+'": '+str(self.komment)
