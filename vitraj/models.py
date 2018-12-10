from django.db import models
class Imgminer(models.Model): #таблица иллюстраций минералов
    MId = models.FloatField(unique=True)
    Name = models.CharField(max_length=50)
class Chemform(models.Model): #таблица химических формул минералов
    MId = models.FloatField(unique=True)
    Name = models.CharField(max_length=50)
    Formula = models.CharField(max_length=150)
class Chemical(models.Model): #таблица химических свойств минералов
    MId = models.FloatField()
    Name = models.CharField(max_length=50)
    Inier = models.IntegerField()
    Val = models.FloatField()
class Ierchem(models.Model): #таблица иерархии химических свойств
    Type = models.IntegerField()
    Minmax = models.CharField(max_length=50)
    Name = models.CharField(max_length=150)
    Abbr = models.CharField(max_length=50)   
    Razm = models.CharField(max_length=10, blank=True)
class Ierin(models.Model): #таблица иерархии интерфейсов
    Type = models.FloatField()
    Name = models.CharField(max_length=150)
class Ierphy(models.Model): #таблица иерархии физических свойств
    Type = models.FloatField()
    Name = models.CharField(max_length=150)
    Razm = models.CharField(max_length=50)
class Interface(models.Model): #таблица интерфейсов
    MId = models.FloatField()
    Name = models.CharField(max_length=150)
    Val = models.FloatField()
class Physic(models.Model): #таблица физических свойств минералов
    MId = models.FloatField()
    Name = models.CharField(max_length=150)
    Ier = models.FloatField()
    Val = models.FloatField(null=True)