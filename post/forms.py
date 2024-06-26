from django import forms
from . import models

class PostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs = {
        'placeholder': 'Enter your title here'
      }),
      'content': forms.Textarea(attrs = {
        'placeholder': 'Enter content here'
      }),
      'categories': forms.CheckboxSelectMultiple()
    }