# paragraphs/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from paragraphs.models import Paragraph, Word, ParagraphWord
from paragraphs.serializers import ParagraphSerializer
from django.db.models import Count


class ParagraphCreateAPIView(generics.CreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

    def perform_create(self, serializer):
        paragraph_text = serializer.validated_data['paragraph_text']
        paragraphs = paragraph_text.split('\n')

        for para_text in paragraphs:
            if para_text.strip():  # Ensure we don't create paragraphs for empty strings
                paragraph = Paragraph.objects.create(
                    paragraph_text=para_text.strip())

                words = para_text.lower().split()
                for word_text in words:
                    word, created = Word.objects.get_or_create(word=word_text)
                    ParagraphWord.objects.get_or_create(
                        paragraph=paragraph, word=word)


class ParagraphSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '').lower()
        results = []

        if query:
            paragraphs = (Paragraph.objects
                          .filter(paragraphword__word__word=query)
                          .annotate(word_count=Count('paragraphword__word'))
                          # Order by count descending and then by ID to ensure consistency
                          .order_by('-word_count', '-id')
                          .distinct()[:10])

            for idx, paragraph in enumerate(paragraphs, start=1):
                results.append(f'paragraph {idx}')

        return Response(results)
