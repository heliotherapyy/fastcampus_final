from django import forms
from mvp.models import Photo, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'image_file',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

