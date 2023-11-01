from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    profle_pic = models.FileField(upload_to="profile/",blank=True,null=True)
    email = models.EmailField()
    user=models.OneToOneField("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    question = models.TextField()
    name = models.ForeignKey("quora.Profile",on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField("auth.User",null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)

    def _str__(self):
        return self.question