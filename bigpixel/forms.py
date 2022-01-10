from django import forms

from bigpixel.models import PixelTrackingCode, PixelTrackingCodeSite


class ShowPixelCodeForm(forms.ModelForm):
    tracking_code = forms.CharField(max_length=140,
                                    widget=forms.Textarea(
                                        attrs={
                                            'class': 'form-control',
                                            'disabled': True,
                                            'rows': 2
                                        }
                                    ))

    class Meta:
        model = PixelTrackingCode
        fields = ('tracking_code',)


class PixelTrackingCodeSiteForm(forms.ModelForm):
    tracking_code = forms.ModelChoiceField(queryset=PixelTrackingCode.objects.all(),
                                           widget=forms.HiddenInput())

    class Meta:
        model = PixelTrackingCodeSite
        fields = ('tracking_code', 'website',)

    def __init__(self, *args, **kwargs):
        super(PixelTrackingCodeSiteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
