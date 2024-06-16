# text_search_app/urls.py
from django.urls import path
from paragraphs.views import ParagraphCreateAPIView, ParagraphSearchAPIView

urlpatterns = [
    path('paragraphs/', ParagraphCreateAPIView.as_view(), name='paragraph-create'),
    path('search/', ParagraphSearchAPIView.as_view(), name='paragraph-search'),
]
