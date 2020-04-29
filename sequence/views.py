from django.shortcuts import render
from django.http import JsonResponse
from .models import (Publications, Sequence)
# Create your views here.

#def index(request):
  #  return render(request, 'sequence/index.html')

def getPublications(request):
    args = {}
    search_type = request.GET['search_type']
    search_text = request.GET['search_text'] if search_type != 'year' else int(request.GET['search_text'])
    args[f"{search_type}__contains" if search_type != 'year' else search_type] = search_text
    final_list = list(Publications.objects.filter(**args).values())
    return JsonResponse(data={'test': 'OK', 'final_list': final_list})

def getSequence(request):
    args = {}
    search_type = request.GET['search_type']
    search_text = request.GET['search_text'] 
    # if search_type != 'year' else int(request.GET['search_text'])
    # args[f"{search_type}__contains" if search_type != 'year' else search_type] = search_text
    args[f"{search_type}__contains"] = search_text
    final_list = list(Sequence.objects.filter(**args).values())
    return JsonResponse(data={'test': 'OK', 'final_list': final_list})

def sequence(request):
    return render(request, 'sequence/sequence.html')

def publications(request):
    return render(request, 'sequence/publications.html')

