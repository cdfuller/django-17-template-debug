from django import forms

class CustomWidget(forms.TextInput):
    def render(self, *args, **kwargs):
        return super(CustomWidget, self).render(*args, **kwargs)

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=CustomWidget)

