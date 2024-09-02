from django.forms.models import ModelForm
from .models import Interest


class InterestModelForm(ModelForm):
    class Meta:
        model = Interest
        fields = 'phone_number', 'message'

    def __init__(self, *args, **kwargs):
        place = kwargs.pop('place', None)
        super().__init__(*args, **kwargs)

        if place:
            self.instance.place = place
