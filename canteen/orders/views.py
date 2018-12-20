from django.shortcuts import render
from .models import Dishes
from django.utils import timezone   
from django.shortcuts import render, get_object_or_404
# Create your views here.
def list_of_dishes(request):
    return render(request, 'orders/view1.html', {})