from django import forms
from django.contrib.auth.models import User
from blog.models import Contact, UserProfile, Category, Post, Feedback, LIKE_CHOICES, Comment, Tag

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name")
    email = forms.EmailField(max_length=75, help_text="Email")
    subject = forms.CharField(max_length=128, help_text="Subject")
    message = forms.CharField(widget=forms.Textarea,help_text="Enter your message here")

    class Meta:
        model = Contact
        fields = ('name','email','subject','message')




class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter category name.")
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Title")
    body = forms.CharField(widget=forms.Textarea, help_text="Your Views")
    category = forms.ModelChoiceField(queryset = Category.objects.all(),help_text="Select Category" )

    class Meta:
        model = Post
        #fields = ('title', 'body', 'category')
        exclude = ['slug']

class TagForm1(forms.ModelForm):
    tag_title = forms.CharField(max_length=100, help_text="Tag Name")
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    post = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tag
        exclude = ['slug']


class TagForm(forms.Form):
    tag_title = forms.CharField(max_length=100, help_text="Use commas to separate tags.")



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ('post','comment_body','commented_on','commenter',)
        exclude =['post', 'commenter']


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text='Name')
    email =forms.EmailField(help_text='Your Email')
    like_dislike = forms.CharField(max_length=2,
                widget=forms.Select(choices=LIKE_CHOICES))

    feedback_msg = forms.CharField(widget=forms.Textarea,help_text="Enter your message here")

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'like_dislike', 'feedback_msg',)
