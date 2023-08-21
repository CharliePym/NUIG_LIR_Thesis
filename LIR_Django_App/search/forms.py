from django import forms  

# user input form class for search query and num judgments
class UserInputForm(forms.Form):
    
    MAX_JUGDMENTS=(('20', '20'), ('50', '50'), ('100', '100'), ('150', '150')) # options for num judgments, num defaults to 20

    search_query = forms.CharField(max_length=200, required=True, label='', 
                                   widget= forms.Textarea(attrs={
                                       'rows':3,
                                       'placeholder':'Enter search query...',
                                       'style': 'width: 400px;'
                                    }))
    
    num_judgments = forms.ChoiceField(choices=MAX_JUGDMENTS, required=False, label='')
    

