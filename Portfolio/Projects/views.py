from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project
from django.template import loader
# from .forms import PortfolioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from embed_video.fields import EmbedVideoField

# Create your views here.
def index(request):
    context = {
        "intro": ""
    }
    return render(request, 'Projects/index.html', context)