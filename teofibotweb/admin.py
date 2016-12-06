from django.contrib import admin

# Register your models here.
from .models import *

class StickerAdmin(admin.ModelAdmin):
	fields = ('label', 'pub_date', ('file_id', 'file_path'),  'image_tag', 'is_cool', ('tags', 'reply_tags'), 'reply', 'specialReply')
	readonly_fields = ('image_tag','pub_date')

admin.site.register(User)
admin.site.register(TextInputPattern)
admin.site.register(AutoResponse)
admin.site.register(Sticker, StickerAdmin)
admin.site.register(Tag)

