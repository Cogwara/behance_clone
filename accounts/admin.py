# admin.py in the "accounts" app

from django.contrib import admin
from .models import Project, UserProfile, Skill, Follow

# Create admin classes for UserProfile, Skill, and Follow
class UserProfileAdmin(admin.ModelAdmin):
    # Customize the displayed fields and other admin options if needed
    list_display = ('user', 'location', 'occupation',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',)

class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')

# Register the models with their respective admin classes
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Project, ProjectAdmin)
