from django.db import models

class NewForm(models.Model):
    SenderName=models.CharField(max_length = 30)
    SenderAddress=models.CharField(max_length = 30)
    RecieverName=models.CharField(max_length = 30)
    RecieverAddress=models.CharField(max_length = 30)
    referenceID=models.CharField(max_length = 30)
    GoodsareFrom=models.CharField(max_length = 30)
    GoodsTo=models.CharField(max_length = 30)
    DepatureDate=models.CharField(max_length = 30)
    Depaturetime=models.CharField(max_length = 30)
    ArrivalDate=models.CharField(max_length = 30)
    ArrivalTime=models.CharField(max_length = 30)
    GoodsDescription=models.TextField(max_length = 1000)
    Status=models.TextField(max_length = 5000)

    def __str__(self):
        return self.referenceID

    @classmethod
    def search_by_referenceID(cls,search_term):
        results = cls.objects.filter(referenceID__icontains=search_term)
        return results


class TrackForms(models.Model):
    ReferenceId =models.CharField(max_length = 30)
    Sender = models.CharField(max_length = 30)
    Reciever = models.CharField(max_length = 30)
    newform = models.ForeignKey(NewForm,on_delete=models.CASCADE)
    def __str__(self):
        return self.ReferenceId


    def save_track(self):
        self.save()

    @classmethod
    def cargo_list(cls):
        scoty = cls.objects()
        return scoty
