from django import forms
from django.core.validators import FileExtensionValidator

from app.models import Channel


class ChannelUpdateForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = [
            'title',
            'group',
            'path',
            'hidden',
        ]


class ChannelCreateForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = [
            'title',
            'path',
            'group',
            'hidden',
        ]


class PlaylistForm(forms.Form):
    url = forms.URLField(
        label='Provide link to playlist',
        required=False
    )
    file = forms.FileField(
        label='Or upload playlist file',
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['m3u8', 'm3u'])]
    )
    remove_existed = forms.BooleanField(
        label='Remove existed channels',
        initial=True,
        required=False
    )

    def clean(self):
        cleaned_data = super(PlaylistForm, self).clean()
        url = cleaned_data.get("url")
        file = cleaned_data.get("file")

        if not url and not file:
            raise forms.ValidationError("You should provide either file or url to your m3u8 playlist")

        return cleaned_data
