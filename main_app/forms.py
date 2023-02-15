from .models import Comment 
from django import forms
from django.forms.widgets import RadioSelect
from .models import Rating




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class RatingForm(forms.ModelForm):
    value = forms.ChoiceField(choices=[(i, f"{i} stars") for i in range(1, 11)], widget=RadioSelect())

    class Meta:
        model = Rating
        fields = ('value',)


