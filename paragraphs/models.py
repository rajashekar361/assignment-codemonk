# text_search_app/models.py
from django.db import models


class Paragraph(models.Model):
    paragraph_text = models.TextField()


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)


class ParagraphWord(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('paragraph', 'word')
