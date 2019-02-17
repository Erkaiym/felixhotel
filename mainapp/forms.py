from django import forms

from mainapp.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['published']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'placeholder': 'Название компании', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Отзыв', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Отзыв', 'class': 'form-control-file'}),
        }
