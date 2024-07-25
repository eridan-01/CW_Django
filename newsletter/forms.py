from django.forms import ModelForm

from newsletter.models import Client, Message, Mailing


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'CheckboxInput':
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


class ClientForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MailingForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'
