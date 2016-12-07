from django.contrib import admin

# Register your models here.
from .models import *


class StickerAdmin(admin.ModelAdmin):
	fields = ('label', 'pub_date', ('file_id', 'file_path'),  'image_tag', 'is_cool', 'tags')
	readonly_fields = ('image_tag','pub_date', 'file_id', 'file_path')


class StickerResponseAdmin(admin.ModelAdmin):
	fields = ('label', 'stickers',  'reply_tags', 'reply', 'specialReply')

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('label', 'type')
	
admin.site.register(User)
admin.site.register(TextInputPattern)
admin.site.register(AutoResponse)
admin.site.register(Sticker, StickerAdmin)
admin.site.register(StickerResponse, StickerResponseAdmin)
admin.site.register(Tag)
admin.site.register(Resource, ResourceAdmin)