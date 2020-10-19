from django.http import JsonResponse
from django.shortcuts import render
from address_book_app.models import Address

def home(request):
    address=Address.objects.all()
    return render(request,'home.html',{'address':address})

def detail(request,pk):
    single_address=Address.objects.get(pk=pk)
    return JsonResponse
