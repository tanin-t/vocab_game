from django.db import models

# Create new table
# 1. create model class in models.py
# 2. Run: python manage.py makemigrations
# 3. Run: python manage.py migrate

# Create your models here.
class VocabSet(models.Model):
    # id = models.IntegerField() --- auto
    name = models.CharField(max_length=200)



class Vocab(models.Model):
    # id --- auto
    vocab = models.CharField(max_length=200)
    vocab_set = models.ForeignKey(VocabSet, on_delete=models.CASCADE)
    part_of_speech = models.CharField(max_length=20)
    meaning = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pictures', blank=True)
    sound = models.FileField(upload_to='sounds', blank=True)
    phonetic = models.CharField(max_length=200)

    def __str__(self):
        return self.vocab + ' - ' + self.meaning
    

class StudentAnswer(models.Model):
    vocab = models.ForeignKey(Vocab, on_delete=models.PROTECT)
    student = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField()