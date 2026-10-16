from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Profile,Project
@require_GET
def portfolio(request):
    p=Profile.objects.order_by('id').first()
    if p is None:return JsonResponse({'error':'Run python manage.py seed_demo'},status=503)
    profile = {k:getattr(p,k) for k in ['name','role','bio','email','image_url']}
    profile['image_url'] = p.image.url if p.image else p.image_url
    projects = []
    for project in Project.objects.prefetch_related('images'):
        data = {k:getattr(project,k) for k in ['id','title','description','category','image_url','demo_url','source_url','is_demo','order']}
        data['image_url'] = project.image.url if project.image else project.image_url
        data.update(content=project.content, technologies=project.technologies, youtube_url=project.youtube_url)
        data['images'] = [{'id':item.id,'image_url':item.image.url,'caption':item.caption} for item in project.images.all()]
        projects.append(data)
    return JsonResponse({'profile':profile,'projects':projects},json_dumps_params={'ensure_ascii':False})
