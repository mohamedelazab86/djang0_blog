from django.contrib import admin
from .models import Post,Comment,Category,ImagePost

class Imageinline(admin.TabularInline):
    model=ImagePost

# customize
class PostAdmin(admin.ModelAdmin):
    list_display=['title','draft']
    list_filter=['publish_date']
    search_fields=['title']
    inlines=[Imageinline]

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)

