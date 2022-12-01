from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import YogaType, YogaClass
from .forms import ReservationForm
import datetime


def mainp(request):
    return render(request, "index.html")


def class_type_list(request):
    yoga_types_list = YogaType.objects.filter(status=1)
    yoga_classes = YogaClass.objects.filter(status=1)
    context = {
        'yoga_types_list': yoga_types_list,
        'yoga_classes': yoga_classes,
        'reservation_form': ReservationForm()
    }
    print("ciao")
    # print(yoga_types_list.values()[0]['title'])
    print("ciao")
    return render(request, "classes.html", context)

