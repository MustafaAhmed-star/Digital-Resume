from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import (Skill,UserProfile
,ContactProfile,Media
,Testimonial,Portfolio
,Blog,Certificate
)


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('id','name','is_active')

admin.site.register(Blog, BlogAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

# @admin.register(Blog,BlogAdmin)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')
#     readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')
