from django.core.management.base import BaseCommand
from devices.models import Category, Model, Problem


# Make device category
def CreateDeviceCategory():
    categoryes = ["Cell Phone", "Tablet"]

    for category in categoryes:
        Category.objects.create(
            name = category
        )
    print("-----Category created-----")



# Make device models
def CreateDeviceModel():
    models = [
        "Samsung Galaxy A13", "Samsung Galaxy S22 Ultra", "Samsung Galaxy S22", "Samsung Galaxy S22+",
        "Samsung Galaxy Z Fold3 5G", "iPhone 13 Pro", "iPhone 13 ProMax", "iPhone 13"
    ]

    for model in models:
        Model.objects.create(
            name = model,
            image = f"modelImage/{model}.png"
        )
    print("-----Models created-----")



# Make device problems
def CreateDeviceProblem():
    problems = ["Back Glass Repair", "Battery Replacement", "Screen Repair"]

    for problem in problems:
        Problem.objects.create(
            name = problem
        )
    print("-----Problems created-----")

class Command(BaseCommand):
    def handle(self, *args, **options):
        CreateDeviceCategory()
        CreateDeviceModel()
        CreateDeviceProblem()