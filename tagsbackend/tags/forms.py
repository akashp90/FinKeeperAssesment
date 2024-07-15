from django import forms
from .models import Post, Tag

class TagForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['tags']

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    new_tags = forms.CharField(
        max_length=200,
        required=False,
        help_text="Enter comma-separated tags."
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'tags', 'new_tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2mm()  # Save the many-to-many data for the form.
        return instance

    def save_m2mm(self):
        self.save_m2m()
        new_tags = self.cleaned_data['new_tags']
        if new_tags:
            tag_names = [tag.strip() for tag in new_tags.split(',')]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                self.instance.tags.add(tag)