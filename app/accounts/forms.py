from django import forms
from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fileld in self.fields.values():
            fileld.widget.attrs.update({'class': 'form-control form-control-lg form-control-alt'})
        self.fields['remember'].widget.attrs.update({'class': 'custom-control-input',})


    def clean(self):
        data = super().clean()
        print(data)
        return data