from django.db import models
from django.utils import timezone

# Create your models here.
class Category_stay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name
class  Payment(models.Model):
    c_payment = models.ForeignKey(Category_stay, on_delete=models.CASCADE,null=True, blank=True) 
    amount=models.IntegerField(null=True, blank=True)
    payno = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10,null=True, blank=True,default='ugx')
    def __int__(self):
      return self.c_payment  
class Babiesform(models.Model):
    c_stay=models.ForeignKey(Category_stay ,on_delete=models.CASCADE,null=True, blank=True)
    c_fees=models.ForeignKey(Payment,on_delete=models.CASCADE,null=True,blank=True)
    name_of_the_baby=models.CharField(max_length=200, blank=True,null=True)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=10, null=True, blank=True)
    age=models.IntegerField(default=0)
    parents_name=models.CharField(max_length=200,null=True, blank=True)
    name_of_the_person_brought_by_the_baby=models.CharField(max_length=200)
    location=models.CharField(max_length=50, null=True, blank=True)
    babys_number=models.IntegerField(default=0 ,null=True, blank=True)
    name_of_the_person_taken_the_baby=models.CharField(max_length=200)
    comment=models.TextField(blank=True,null=True )
    timein=models.TimeField(null=False, blank=False)
    timeout=models.TimeField(null=False, blank=False)

    def __str__(self):
        return self.name_of_the_baby
    
    # class Login(models.Model):
    #         username=models.CharField(max_length=200)
    #         password=models.CharField(max_length=200)
    #         def __str__(self):
    #             return self.username
            
