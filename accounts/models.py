# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     website = models.URLField(blank=True)
#     avatar = models.ImageField(upload_to='user_avatars/', blank=True, null=True)
#     social_links = models.JSONField(blank=True, null=True)
#     skills = models.ManyToManyField('Skill', related_name='user_profiles', blank=True)
#     projects = models.ManyToManyField('Project', related_name='contributors', blank=True)

#     # Additional fields:
#     location = models.CharField(max_length=255, blank=True)
#     occupation = models.CharField(max_length=255, blank=True)
#     followers = models.ManyToManyField(User, through='Follow', related_name='following_profiles')
#     # Add any other user-specific fields here

#     def __str__(self):
#         return self.user.username


# class Follow(models.Model):
#     ffollower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
#     following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
#     created_at = models.DateTimeField(auto_now_add=True)

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    other_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='user_avatars/', blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    skills = models.ManyToManyField('Skill', related_name='user_profiles', blank=True)
    projects = models.ManyToManyField('Project', related_name='contributors', blank=True)

    # Additional fields:
    location = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# Create a Follow model to represent followers and following
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    created_at = models.DateTimeField(auto_now_add=True)