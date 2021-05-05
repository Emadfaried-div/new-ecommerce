from django.contrib import admin
from ecomapp.models import Setting, ContactMessage,FAQ

# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)

class FAQAdmin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'created_at', 'updated_at']

admin.site.register(FAQ,FAQAdmin)

