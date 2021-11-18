from django import forms

from polls.models import PollUnit


class AddPollUnitForm(forms.ModelForm):
    class Meta:
        model = PollUnit
        fields = "__all__"
