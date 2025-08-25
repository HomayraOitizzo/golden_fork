from django.shortcuts import render
from django.http import HttpResponse
from .models import Item_list,Items,Feedback,BookTable
# Create your views here.

def home(request):
  
    review = Feedback.objects.all()
    return render(request, 'home.html',{ 'review': review})

def about(request):
    return render('','about.html')

def menu(request):
    Category = request.GET.get('Category')

    if Category:
        items = Items.objects.filter(Category__Category_name=Category)
    else:
        items = Items.objects.all()

    # Use Item_list to fetch all category objects
    categories = Item_list.objects.all()
    return render(request, 'menu.html', {
        'items': items,
        'categories': categories,
        'Category': Category,
    })

def book(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        booking_date = request.POST.get('booking_date')
        total_person = request.POST.get('total_person')

        if name != '' and email != '' and len(phone_number)==10 and booking_date!='' and total_person!='':
            data = BookTable(Name=name, Phone_number = phone_number, Email=email, Total_person=total_person,
                             Booking_date=booking_date)
            data.save()
    
    return render(request, 'book.html')

def feedback(request):
    return render('', 'feedback.html')


def login(request):
    return render('', 'login.html')