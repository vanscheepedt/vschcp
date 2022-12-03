from django.forms import ModelForm

from .models import Article, Author


class AuthorForm(ModelForm):
    """
    Form for author creation
    """
    class Meta:
        model = Author
        fields = ['name', 'bio']


class ArticleForm(ModelForm):
    """
    Form for article submission
    """
    class Meta:
        model = Article
        fields = ['title', 'summary', 'article']
