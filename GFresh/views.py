from django.shortcuts import render,redirect
from features.models import features
from products.models import products
from categories.models import categories
from reviews.models import reviews
from blogs.models import blogs
from subscribe.models import subscribe

from django.core.mail import send_mail

def search(request):
    return render(request,"index.html",data)

def login(request):
    return render(request,"login.html")


def savesubscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        en = subscribe(sub_email=email)
        en.save()
        send_mail(
            "Thanks! successfully Connected to GFresh ! ",
            "You Can Order Every Item on GFresh is Fresh, Fast Delivery, Easy Payment !",
            "gfresh2024@gmail.com",
            [email],
            fail_silently=False,
        )
    
    return redirect('index')


def aboutus(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")


    
def index(request):
    features_data = features.objects.all()
    products_data = products.objects.all()
    categories_data = categories.objects.all()
    reviews_data = reviews.objects.all()
    blogs_data = blogs.objects.all()


    data = {
        'features_data':features_data,
        'products_data':products_data,
        'categories_data':categories_data,
        'reviews_data':reviews_data,
        'blogs_data':blogs_data
    }
    return render(request,"index.html",data)

