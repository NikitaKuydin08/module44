from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse


def index(request):
     title = request.GET.get('query')

     if title:
          ads = Advertisement.objects.filter(title__icontains=title)
     else:
          ads = Advertisement.objects.all()
     context = {'advertisements': ads, 'title': title}
     return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')



def advertisement_post(request):
     if request.method == "POST":
          form = AdvertisementForm(request.POST, request.FILES)
          if form.is_valid():
               adv = Advertisement(**form.cleaned_data)
               adv.user = request.user
               adv.save()
               url = reverse('main-page')
               return redirect(url)

     else:
          form = AdvertisementForm()

     context = {'form': form}
     return render(request, 'app_advertisements/advertisement-post.html', context)


def advertisement_detail(request, pk):
     ads = Advertisement.objects.get(id=pk)
     context = {'advertisement': ads}
     return render(request, 'app_advertisements/advertisement.html', context)