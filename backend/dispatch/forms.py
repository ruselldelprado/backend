from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):

    
    class Meta:
        model = Incident
        fields = '__all__'

        labels = {
            'date' : 'Date',
            'time_of_call' : 'Time of Call' ,
            'details' : 'Details' ,
            'caller' : 'Caller',
            'address' : 'Address' ,
            'contact_number' : 'Contact Number' ,
            'action_taken' : 'Action Taken' ,
            'time_of_dispatch' : 'Time of Dispatch',
            'responded_by' : 'responded by' ,
            'back_to_base' : 'Back to Base' ,
            'radio_or_telephone' : 'Radio/Telephone',
            'remarks' : 'Remarks' ,
        }

        widgets  = {
            'date' : forms.DateInput(attrs={'placeholder': 'date' ,"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'time_of_call' : forms.TimeInput(attrs={'placeholder': 'time_of_call',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'details' : forms.TimeInput(attrs={'placeholder': 'Details',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'caller' : forms.TextInput(attrs={'placeholder': 'caller',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'address' : forms.TextInput(attrs={'placeholder': 'address',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'contact_number' : forms.NumberInput(attrs={'placeholder': 'contact_number',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'action_taken' : forms.TextInput(attrs={'placeholder': 'action_taken',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'time_of_dispatch' : forms.TimeInput(attrs={'placeholder': 'time_of_dispatch',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'responded_by' : forms.TextInput(attrs={'placeholder': 'responded_by',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'back_to_base' : forms.TimeInput(attrs={'placeholder': 'back_to_base',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'radio_or_telephone' : forms.TextInput(attrs={'placeholder': 'radio_or_telephone',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
            'remarks' : forms.TextInput(attrs={'placeholder': 'remarks',"class": "h-10 border mt-1 rounded px-4 w-full bg-gray-50"}),
        }
        