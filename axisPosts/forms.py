from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisPosts.models import Post
from axisPMS.models import pmsPost

class uploadPostForm(forms.ModelForm):
    postTitle = forms.CharField(label='postTitle',required=True,
                                help_text='Title of this Post',
                                widget=forms.TextInput(attrs={'placeholder': 'Post Title'}))
    postAuthor = forms.CharField(label='postAuthor',required=False)
    content = forms.CharField(label='content',required=True,
                                help_text='Description of the Post',
                                widget=forms.Textarea(attrs={'placeholder': 'Post Description'}))
    categoryChoices = [('0', 'Regular Post'),('1', 'Project'),('2', 'Complaint'),('3', 'Concern'),('4', 'Movement'),('5', 'Awareness')]
    category = forms.ChoiceField (label='category',required=False,
                                widget=forms.Select(attrs={'title': 'Post Category'}),choices=categoryChoices)
    axisStatusChoices = [('0', 'None'),('1', 'Planning Phase'),('2', 'On Going'),('3', 'Suspended'),('4', 'Completed/Ended'),('5','Cancelled')]
    axisStatus = forms.ChoiceField (label='axisStatus',required=False,
                                widget=forms.Select(attrs={'title': 'Issue Status'}),choices=axisStatusChoices)
    postLevelChoices = [('0', 'None'),('1', 'Government'),('2', 'Community'),('3', 'Private'),('4', 'Charity'),('5','Organization')]
    postLevel = forms.ChoiceField (label='axisStatus',required=False,
                                widget=forms.Select(attrs={'title': 'Issue Status'}),choices=postLevelChoices)
    budget = forms.IntegerField(label='budget',required=False,initial=0,
                                widget=forms.NumberInput(attrs={'placeholder': 'Budget'}))
    startDate = forms.DateField(label='startDate',required=False,
                                widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    endDate = forms.DateField(label='endDate',required=False,
                                widget=AdminDateWidget)
    image=forms.ImageField( required=False)


    class Meta:
        model = Post
        fields = ["postTitle","content","category","axisStatus","postLevel","budget","startDate","endDate"]
