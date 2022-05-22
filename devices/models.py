from django.db import models

# Create your models here.
# Device category model
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


# Device model Model
class Model(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=False, blank=False, upload_to='modelImage',)

    def __str__(self):
        return f"{self.name}"


# Device problems
class Problem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


# Devices
class Device(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    problems =  models.ManyToManyField(
        Problem,
        related_name='phoenproblems',
        null=True, blank=True,
    )
    models = models.ManyToManyField(
        Model,
        related_name='phonemodel',
        null=True, blank=True,
    )

    def __str__(self):
        return f"{self.name}"