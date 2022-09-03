from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Blog(models.Model):
    audio_choice = (
    ("Processing", "Processing"),
    ("Complete", "Complete")
)
    title = models.CharField(max_length=100)
    content = RichTextField()
    audio_url = models.FileField(upload_to = 'audio_file/', null=True, blank=True)
    audio_status = models.CharField(choices=audio_choice, max_length=15)
    state = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    slug = models.SlugField(max_length=40)

    # class Meta:
    #     unique_together = ('user', 'title',)

    def __str__(self):
        return self.title

class Tag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.blog)