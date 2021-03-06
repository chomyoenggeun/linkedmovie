from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    exclude = ('like_users',)

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)