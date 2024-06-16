
from rest_framework import serializers
from paragraphs.models import Paragraph


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['paragraph_text']
