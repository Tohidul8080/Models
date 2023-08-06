from django.shortcuts import render
from django.http import HttpResponse
from Mapps.models import Musician, Album
from Mapps import forms

# Create your views here.

def Base(request):
    musician_list=Musician.objects.order_by('first_name')
    album_list=Album.objects.order_by('name')
    diction={'text_1':"This is First table", 'musician':musician_list,'album':album_list,'text_2':"This is Second Table"}
    return render(request, 'index.html', context=diction)

def form(request):
    new_form=forms.user_form()
    diction={'test_form':new_form,'heading_3':"this is form"}

    if request.method == 'POST':
        new_form=forms.user_form(request.POST)

        if new_form.is_valid():
            user_nam=new_form.cleaned_data['user_name']
            user_do=new_form.cleaned_data['user_dob']
            user_emai=new_form.cleaned_data['user_email']

            diction.update({'user_n':user_nam})
            diction.update({'user_d':user_do})
            diction.update({'user_e':user_emai})
            diction.update({'form_submit':'yes'})

    



    return render(request,'form.html',context=diction)
