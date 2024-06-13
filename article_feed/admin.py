from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(post, PostAdmin)
#admin.site.register(postCategory, CategoryAdmin)
admin.site.register(faq)
admin.site.register(docs)
admin.site.register(reportsGroup)
#admin.site.register(docsInPost)
#admin.site.register(postContent)
#admin.site.register(postContentType)
admin.site.register(products)
admin.site.register(dataFromForms)


# Register your models here.
