# admin.py
#modelの追加、編集、削除

from django.contrib import admin
from .models import Post

admin.site.register(Post)


