from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
	list_display = ("name", "branch", "gender", "date_of_birth", "race", "reporter")
	list_filter = ("branch", "gender", "race")
	search_fields = ("name",)
	list_editable = ("gender", "race")

admin.site.register(Invite, InviteAdmin)

# Register your models here.
