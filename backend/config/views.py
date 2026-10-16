import mimetypes
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
from django.utils._os import safe_join
from django.core.exceptions import SuspiciousFileOperation
from django.db import connection
from django.views.decorators.http import require_GET


@require_GET
def frontend(request):
    path = settings.FRONTEND_DIST / 'index.html'
    if not path.is_file():
        raise Http404('Build frontend first: npm run build')
    return FileResponse(path.open('rb'), content_type='text/html')


@require_GET
def uploaded_image(request, name):
    try:
        path = Path(safe_join(settings.MEDIA_ROOT, name))
    except SuspiciousFileOperation:
        raise Http404
    content_type = mimetypes.guess_type(str(path))[0]
    if content_type not in {'image/jpeg','image/png','image/webp','image/gif','image/avif','image/bmp','image/tiff','image/x-icon'} or not path.is_file():
        raise Http404
    return FileResponse(path.open('rb'),content_type=content_type)


@require_GET
def health(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
    return JsonResponse({'status':'ok'})
