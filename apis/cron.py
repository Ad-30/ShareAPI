import datetime
from django.utils import timezone
from .models import FileModel


def delete_expired_files():
    expiration_time = timezone.now() - datetime.timedelta(minutes=10)
    expired_files = FileModel.objects.filter(created_at__lte=expiration_time)

    for file in expired_files:
        file.file.delete()
        file.delete()
