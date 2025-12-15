from django.shortcuts import render
from vocab.models import Vocab, VocabSet
from django.http import JsonResponse

def welcome(request):
    return render(
        request, 
        'vocab/welcome.html'
    )


# Create your views here.
def learn_word(request, vocab_set_id, vocab_index):

    vocab = Vocab.objects.filter(vocab_set_id=vocab_set_id)[vocab_index]
    next_index = vocab_index + 1
    prev_index = vocab_index - 1
    total_index = Vocab.objects.filter(vocab_set_id=vocab_set_id).count() - 1
    return render(
        request, 
        'vocab/learn_word.html', # file ที่จะแสดง
        {
            'vocab': vocab,
            'next_index': next_index,
            'prev_index': prev_index,
            'vocab_index': vocab_index,
            'total_index': total_index
        } # ข้อมูลที่จะส่งไป file html
    )

def choose_vocab_set(request):
    vocab_sets = VocabSet.objects.all()
    return render(
        request,
        'vocab/choose_vocab_set.html',
        {"vocab_sets": vocab_sets}
    )