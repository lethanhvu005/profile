from django.contrib import admin
from django.utils.html import format_html
from .models import Profile,Project,ProjectImage

class ProjectImageInline(admin.TabularInline):
    model=ProjectImage
    extra=1
    readonly_fields=['preview']

    @admin.display(description='Xem trước')
    def preview(self,obj):
        if not obj.image:
            return 'Chưa có ảnh'
        return format_html('<img src="{}" style="max-width:160px;max-height:110px" alt="">',obj.image.url)
class ImagePreviewAdmin(admin.ModelAdmin):
    readonly_fields=['image_preview']

    @admin.display(description='Xem trước ảnh')
    def image_preview(self,obj):
        url = obj.image.url if obj.image else obj.image_url
        if not url:
            return 'Chưa có ảnh'
        return format_html('<img src="{}" style="max-width:300px;max-height:220px;object-fit:contain" alt="Ảnh xem trước">',url)

@admin.register(Profile)
class ProfileAdmin(ImagePreviewAdmin):
    list_display=['name','role','email']
    def has_add_permission(self,request):return not Profile.objects.exists()
@admin.register(Project)
class ProjectAdmin(ImagePreviewAdmin):
    inlines=[ProjectImageInline]
    list_display=['title','category','is_demo','order']
    list_filter=['category','is_demo']
    search_fields=['title']
