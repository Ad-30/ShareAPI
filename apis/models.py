# from django.db import models
# # from django_cleanup import mixins as cleanup_mixins


# class FileModel(models.Model):
#     file = models.FileField(upload_to='files/')
#     unique_code = models.CharField(max_length=6, blank=True)

#     def __str__(self):
#         return self.file.name
from django.db import models
from django_cleanup.signals import cleanup_pre_delete
from django.dispatch import receiver


class FileModel(models.Model):
    file = models.FileField(upload_to='files/')
    unique_code = models.CharField(max_length=6, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


@receiver(cleanup_pre_delete, sender=FileModel)
def delete_file_on_delete(sender, instance, **kwargs):
    instance.file.delete(save=False)
