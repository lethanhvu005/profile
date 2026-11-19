from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from portfolio.models import Project

PROJECT_COVERS = [
    ('NEXA GEAR / CommerceOS', 'nexa-commerceos.jpg'),
    ('SafeVision — AI Driver Safety System', 'safevision.jpg'),
]


class Command(BaseCommand):
    help = 'Attach real cover screenshots to portfolio projects without replacing existing covers.'

    def handle(self, *args, **options):
        assets = settings.BASE_DIR / 'demo_assets'
        for title, filename in PROJECT_COVERS:
            project = Project.objects.filter(title=title).first()
            path = assets / filename
            if not project or not path.exists():
                self.stdout.write(f'Skipped: {filename}')
                continue
            if not project.image and not project.image_url:
                with path.open('rb') as stream:
                    project.image.save(path.name, File(stream), save=True)
                self.stdout.write(self.style.SUCCESS(f'Cover ready: {filename}'))
            else:
                self.stdout.write(f'Exists: {filename}')


