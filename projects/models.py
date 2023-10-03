from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='project_covers/', blank=True, null=True)
    images = models.ManyToManyField('ProjectImage', related_name='project_images', blank=True)
    appreciations = models.ManyToManyField(User, through='Appreciation', related_name='appreciated_projects')
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_projects')

    # Additional fields:
    categories = models.ManyToManyField('Category', related_name='projects', blank=True)
    tags = models.ManyToManyField('Tag', related_name='projects', blank=True)
    project_url = models.URLField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    # Add any other project-specific fields here

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

class Appreciation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Appreciation'
        verbose_name_plural = 'Appreciations'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

