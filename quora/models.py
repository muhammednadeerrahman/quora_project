from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    profle_pic = models.FileField(upload_to="profile/",blank=True,null=True)
    email = models.EmailField()
    user=models.OneToOneField("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.name