from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from address_book_app.models import Address

def home(request):
    address=Address.objects.all()
    return render(request,'home.html',{'address':address})

def detail(request,pk):
    single_address=Address.objects.get(pk=pk)
    print("single address")
    return render(request,'details.html',{'address':single_address})

def search(request):
    if request.method=='POST':
        query=request.POST.get('name')
        results=Address.objects.filter(name__icontains=query)
        return render(request,'search_results.html',{'address':results})
    else:
        return HttpResponse
