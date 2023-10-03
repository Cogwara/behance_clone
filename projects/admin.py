from django.contrib import admin
from .models import Appreciation, Category, Comment, Project, ProjectImage, Tag

# Create an admin class for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')  # Customize the displayed fields

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'text',)

@admin.register(Appreciation)
class ApprociationAdmin(admin.ModelAdmin):
    list_display = ('user', 'project',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    


# Register the models with their respective admin classes
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
