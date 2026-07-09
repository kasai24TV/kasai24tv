from django.db import models

class Video(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField()
    publie = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
