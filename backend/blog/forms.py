from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from blog.models import Post
from users.models import User

class AddressForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(
        # label='Text',
        widget=forms.Textarea(attrs={'placeholder': 'Text'})
    )
    main_img = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('main_img', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('text', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Create')
        )
