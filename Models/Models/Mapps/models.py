from django.db import models

# Create your models here.

class Musician(models.Model):
   #id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20, null=True, blank=True)
    last_name=models.CharField(max_length=20)
    instrument=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name+" "+ self.last_name



class Album(models.Model):
   # id =models.AutoField(Primary_key=True)
    artis=models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    Rating=(
        (1,"Good"),
        (2,"Bad"),
        (3,"Not Good"),
        (4, "Excelent"),
        (5, "WOW"),
    )
    num_stars=models.IntegerField(choices=Rating)

    def __str__(self):
        return self.name+ "Rating: "+ str(self.num_stars)

