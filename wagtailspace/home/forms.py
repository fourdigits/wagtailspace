from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import HTML, Div, Field
from django import forms
from .models import Registration


class SignupForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'full_name',
            'email',
            'github_nickname',
            'company',
            'dates',
            'food_allergies',
            'roles',
            'shirt_size',
            'give_a_talk',
            'talk_title',
            'comments',
        ]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['dates'].widget = forms.CheckboxSelectMultiple()
        self.fields['roles'].widget = forms.CheckboxSelectMultiple()
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('full_name'),
            Field('email'),
            Field('github_nickname'),
            Field('company'),
            Field('dates', css_class="dates-attending"),
            Field('food_allergies'),
            Field('roles'),
            Field('shirt_size'),
            Field('give_a_talk', css_class='give_a_talk'),
            Field('talk_title', css_class='talk_title'),
            Field('comments'),
        )
