from django.shortcuts import render
from django.http import HttpResponse

from .models import Phone


# Create your views here.
def phones_magazine(request):
    sort = request.GET.get('sort', 'name')

    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    return render(request, 'phones_magazine/phones.html', {'phones': phones})

def phone_detail(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'phones_magazine/phone_detail.html', {'phone': phone})