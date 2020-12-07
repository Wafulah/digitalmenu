import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Meal(models.Model):
    meal_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.meal_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Drinks(models.Model):
    drinks_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.drinks_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Price(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    price_text = models.CharField(max_length=200)

    def __str__(self):
        return self.price_text




