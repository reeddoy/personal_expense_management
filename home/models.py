from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    STATUS_CHOICES = [
        ('trial', 'Trial'),
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=50, blank=True, null=True)
    security_code = models.CharField(max_length=50, blank=True, null=True)
    email_notification = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='trial')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, default='profile/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


class Create_Expense_Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_by = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    


class Tour_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    tour_date = models.DateField(blank=True,null=True, auto_now=False)
    tour_code = models.CharField(max_length=50,blank=True,null=True)
    total_cost = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True,null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Loan_Given_Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True,null=True)
    total_paid = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True,null=True)
    total_due = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True,null=True)
    loan_user_code = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name
    


class Expense_List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    tour_expense = models.BooleanField(default=False)
    loan_expense = models.BooleanField(default=False)
    tour_code = models.CharField(max_length=50,blank=True,null=True)
    loan_code = models.CharField(max_length=50,blank=True,null=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True,null=True)
    note = models.TextField(blank=True, null=True)
    expense_by = models.CharField(max_length=100, blank=True, null=True)   #cash or bank
    created_by = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class Income_List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    loan_income = models.BooleanField(default=False)
    loan_code = models.CharField(max_length=50,blank=True,null=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True,null=True)
    note = models.TextField(blank=True, null=True)
    income_get_by = models.CharField(max_length=100, blank=True, null=True)   #cash or bank
    created_by = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name