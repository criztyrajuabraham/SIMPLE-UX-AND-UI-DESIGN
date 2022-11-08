
from django import forms


from .models import Details


class detailsform(forms.ModelForm):
    class Meta:
        model= Details
        fields= ['username' ,'dateofbirth' ,'age','gender' ,'phone', 'mail',
                 'comments' ,'parent_selection' ,'child_selection', 'user_interest']

