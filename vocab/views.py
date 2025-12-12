from django.shortcuts import render
from vocab.models import Vocab
from django.http import JsonResponse

def welcome(request):
    return render(
        request, 
        'vocab/welcome.html'
    )


# Create your views here.
def learn_word(request, pk):
    vocab = Vocab.objects.get(id=pk)
    return render(
        request, 
        'vocab/learn_word.html', # file ที่จะแสดง
        {'vocab': vocab} # ข้อมูลที่จะส่งไป file html
    )

