from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.
def demo(request):
    if request.method=='POST':
        new_link=request.POST.get('page')
        url=requests.get(new_link)
        simple=BeautifulSoup(url.text,'html.parser')
        for links in simple.find_all('a'):
            links_address = links.get('href')
            links_string= links.string
            Link.objects.create(address=links_address,string_name=links_string)
        return redirect('/')
    else:
          li_database=Link.objects.all()
    return render(request,'index.html',{'li':li_database})