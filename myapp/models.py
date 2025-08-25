from django.db import models

# Create your models here.
class Item_list(models.Model):
    Category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.Category_name


class Items(models.Model):
    Items_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(Item_list, related_name='category_name', on_delete=models.CASCADE)
    Image = models.ImageField()
    
    def __str__(self):
        return self.Items_name

class Aboutus(models.Model):
    Description=models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(blank=True)

class BookTable(models.Model):
    Name = models.CharField(max_length=20)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField(null=True)

