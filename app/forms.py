from django import forms

class CreateArticleForm(forms.Form):
    ARTICLE_STATUS = (
        ("draft", "Draft"),
        ("in progress", "In progress"),
        ("published", "Published"),
    )

    title = forms.CharField(max_length=200)
    status = forms.ChoiceField(choices=ARTICLE_STATUS)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField(widget=forms.Textarea, required=False)