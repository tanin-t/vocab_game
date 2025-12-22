from django.shortcuts import render, redirect
from vocab.models import StudentAnswer, Vocab, VocabSet
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def welcome(request):
    return render(
        request, 
        'vocab/welcome.html'
    )


# Create your views here.
@login_required
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


@login_required
def choose_vocab_set(request):
    vocab_sets = VocabSet.objects.all()
    return render(
        request,
        'vocab/choose_vocab_set.html',
        {"vocab_sets": vocab_sets}
    )

import random

@login_required
def game_eng_thai(request):
    vocab_ids = Vocab.objects.all().values_list('id', flat=True)
    random_vocab_id = random.choice(vocab_ids)
    vocab = Vocab.objects.get(id=random_vocab_id)

    vocab_ids = list(vocab_ids)
    vocab_ids.remove(random_vocab_id)

    choice_ids = random.sample(vocab_ids, k=3)
    choices = Vocab.objects.filter(id__in=choice_ids)
    choices = list(choices)

    choices.append(vocab)
    random.shuffle(choices)

    return render(request, 'vocab/game_eng_thai.html', 
                  {'vocab': vocab, 'choices': choices})

@login_required
def game_eng_thai_answer(request):
    print(request.POST)
    vocab_id = request.POST['vocab']
    vocab = Vocab.objects.get(id=vocab_id)
    answer = request.POST['answer']

    # save student answer
    sa = StudentAnswer()
    sa.vocab = vocab
    sa.student = request.user
    sa.is_correct = vocab.meaning == answer
    sa.answer = answer
    sa.save()

    # show correct / incorrect
    return HttpResponse("OK")