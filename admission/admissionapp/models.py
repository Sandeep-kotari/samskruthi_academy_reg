from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    batch_start_day = models.DateField()
    class_name = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    alternate_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    tution_fee = models.DecimalField(max_digits=10, decimal_places=2)
    dp_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    emi = models.CharField(max_length=255)
    emi_per_month = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.student_name