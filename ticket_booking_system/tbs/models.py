from django.db import models

# Create your models here.
class Person(models.Model):
    p_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.p_id

class Movie(models.Model):
    m_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.m_id

class Ticket(models.Model):
    t_id = models.AutoField(primary_key=True)
    expired=models.BooleanField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start_time=models.CharField(max_length=20)
    movie = models.OneToOneField(Movie,
                                 default=False,
                                 on_delete=models.CASCADE)
    end_time = models.CharField(max_length=20)

    def __str__(self):
        return self.t_id




