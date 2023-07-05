from django.contrib import admin
from newresume.models import Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=['id','name','contact','email','school','degree','skills','about_you','experience']
    
admin.site.register(Users,UsersAdmin)