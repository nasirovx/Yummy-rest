from django.forms import ModelForm, Textarea, TextInput, FileInput,\
    EmailInput, PasswordInput, Select, DateInput, TimeInput, NumberInput
from .models import Book_A_Table, Contact


class Book_A_TableForm(ModelForm):
    class Meta:
        model = Book_A_Table
        fields = ['full_name', 'email', 'phone', 'date',
                   'time', 'people', 'message']
        widgets = {
            "full_name": TextInput(attrs={
                "type": "text",
                "name": "name",
                "class": "form-control",
                "id": "name",
                "placeholder": "Your Name",
                "data-rule": "minlen:4",
                "data-msg": "Please enter at least 4 chars"
            }),
            "email": EmailInput(attrs={
                "type": "email",
                "class": "form-control",
                "name": "email",
                "id": "email",
                "placeholder": "Your Email",
                "data-rule": "email",
                "data-msg": "Please enter a valid email"
            }),
            "phone": TextInput(attrs={
                "type": "text",
                "class": "form-control",
                "name": "phone",
                "id": "phone",
                "placeholder": "Your Phone",
                "data-rule": "minlen:4",
                "data-msg": "Please enter at least 4 chars"
            }),
            "date": DateInput(attrs={
                "name": "date",
                "class": "form-control",
                "id": "date",
                "placeholder": "Date",
                "data-rule": "minlen:4",
                "data-msg": "Please enter at least 4 chars"
            }),
            "time": TimeInput(attrs={
                "name": "time",
                "class": "form-control",
                "id": "time",
                "placeholder": "Time",
                "data-rule": "minlen:4",
                "data-msg": "Please enter at least 4 chars"
            }),
            "people": NumberInput(attrs={
                "type": "number",
                "class": "form-control",
                "name": "people",
                "id": "people",
                "placeholder": "# of people",
                "data-rule": "minlen:1",
                "data-msg": "Please enter at least 1 chars"
            }),
            "message": Textarea(attrs={
                "class": "form-control",
                "name": "message",
                "rows": "5",
                "placeholder": "Message",
            }),
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            "full_name": TextInput(attrs={
                "type": "text",
                "name": "name",
                "class": "form-control",
                "id": "name",
                "placeholder": "Your Name",
            }),
            "email": EmailInput(attrs={
                "type": "email",
                "class": "form-control",
                "name": "email",
                "id": "email",
                "placeholder": "Your Email",
            }),
            "subject": TextInput(attrs={
                "type": "text",
                "class": "form-control",
                "name": "subject",
                "id": "subject",
                "placeholder": "Subject",
            }),
            "message": Textarea(attrs={
                "class": "form-control",
                "name": "message",
                "rows": "5",
                "placeholder": "Message",
            }),
        }
