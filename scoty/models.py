from django.db import models

class NewForm(models.Model):
    SenderName=models.CharField(max_length = 250)
    SenderAddress=models.CharField(max_length = 250)
    RecieverName=models.CharField(max_length = 250)
    RecieverAddress=models.CharField(max_length = 250)
    referenceID=models.CharField(max_length = 250)
    GoodsareFrom=models.CharField(max_length = 250)
    GoodsTo=models.CharField(max_length = 250)
    DepatureDate=models.CharField(max_length = 250)
    Depaturetime=models.CharField(max_length = 250)
    ArrivalDate=models.CharField(max_length = 250)
    ArrivalTime=models.CharField(max_length = 250)
    GoodsDescription=models.TextField(max_length = 1000)
    Status=models.TextField(max_length = 5000)

    def __str__(self):
        return self.referenceID

    @classmethod
    def search_by_referenceID(cls,search_term):
        results = cls.objects.filter(referenceID__icontains=search_term)
        return results


class TrackForms(models.Model):
    ReferenceId =models.CharField(max_length = 250)
    Sender = models.CharField(max_length = 250)
    Reciever = models.CharField(max_length = 250)
    newform = models.ForeignKey(NewForm,on_delete=models.CASCADE)
    def __str__(self):
        return self.ReferenceId


    def save_track(self):
        self.save()

    @classmethod
    def cargo_list(cls):
        scoty = cls.objects()
        return scoty
