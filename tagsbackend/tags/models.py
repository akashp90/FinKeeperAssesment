from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    @property
    def tag_names(self):
    	return ','.join(self.tags.order_by("name").values_list('name', flat=True))
    

    def _str_(self):
        return self.title
