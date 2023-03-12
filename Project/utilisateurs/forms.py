from django import forms
from .models import Utilisateur


List_revues = (
    ('S', 'Scopus'),
    ('P', 'PubMed'),
    ('D', 'Dimensions'),
    ('W', 'Web Of Science')
)

class UtilisateurForm(forms.ModelForm):
    nom          = forms.CharField()
    prenom       = forms.CharField()
    mail         = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "put a valid email adress "}))
    revues       = forms.MultipleChoiceField(choices=List_revues)

    class Meta:
        model = Utilisateur
        fields = ['nom','prenom','mail', 'revues']
