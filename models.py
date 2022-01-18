from django.db import models

# Create your models here.
class student(models.Model):
    name=models.Charfield(max_length=100)
    GENDER = (
        ("f","female"),
        ("m","male"),
    )
    roll_number =models.Intergerfield(unique = true)

    email = models.Emailfield(max_length=100)
    gender = models.Charfield(max_length=1, choices = GENDERS)
    percentage = models.floatflied()
    institute= models.foreignkey("Institute", on_delete=models.CASCADE,null=true, bland = true)
    class Institute(models.model):
        types = (
            ("c","college"),
            ("h","high school")
        )
        name=models.charfield(max_length=200)
        type_of_institude = models.charfield(max_length=1,choices = TYPES)



