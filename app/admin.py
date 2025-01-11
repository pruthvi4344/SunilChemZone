from django.contrib import admin
# from .models import signup
# Register your models here.
# admin.site.register(signup)
from .models import Standard, Chapter, StudyMaterial, Post, myphoto,myinfo, skills

admin.site.register(Standard)
admin.site.register(Chapter)
admin.site.register(StudyMaterial)
admin.site.register(Post)
admin.site.register(myphoto)
admin.site.register(myinfo)
admin.site.register(skills)