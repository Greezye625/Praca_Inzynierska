from django.contrib import admin
from threads.models import Thread, ThreadComment, ThreadCategory

admin.site.register(Thread)
admin.site.register(ThreadComment)
admin.site.register(ThreadCategory)

# Register your models here.
