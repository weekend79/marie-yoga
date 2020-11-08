from django import forms


class OrderForm(forms.Form):
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    course_date = forms.CharField(required=True)
    course_time = forms.CharField(required=True)
    order_message = forms.CharField(widget=forms.Textarea)
