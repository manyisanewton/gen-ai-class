from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # ✅ Removed 'updated_at'
    search_fields = ('title', 'body')             # ✅ Fixed 'content' → 'body'
    readonly_fields = ('created_at',)
    list_filter = ('title', 'created_at')         # ✅ Removed invalid fields
    ordering = ('-created_at',)
