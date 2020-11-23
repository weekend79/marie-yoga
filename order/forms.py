from django import forms


# My forms 
class OrderForm(forms.Form):
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    course_name = forms.CharField()
    course_date = forms.CharField()
    course_time = forms.CharField()
    order_message = forms.CharField(widget=forms.Textarea)
