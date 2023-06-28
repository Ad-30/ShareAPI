from rest_framework import serializers
from .models import FileModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('file',)

    def create(self, validated_data):
        file = validated_data.get('file')
        return FileModel.objects.create(file=file)
