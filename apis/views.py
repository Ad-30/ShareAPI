import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FileModel
from .serializers import FileSerializer
import os
from django.http import FileResponse
from .cron import delete_expired_files
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(APIView):
    def post(self, request, format=None):
        delete_expired_files()
        file_serializer = FileSerializer(
            data=request.data, many=True)
        if file_serializer.is_valid():
            unique_code = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=6))

            for file_data in request.FILES.getlist('file'):
                file_instance = FileModel(
                    file=file_data, unique_code=unique_code)
                file_instance.save()

            print(unique_code)
            return Response({'unique_code': unique_code, 'message': "success"}, status=201)
        else:
            return Response(file_serializer.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class FileDownloadView(APIView):
    def get(self, request, unique_code, format=None):
        files = FileModel.objects.filter(unique_code=unique_code)
        delete_expired_files()
        if files.exists():
            file_list = []

            for file in files:
                file_path = file.file.path
                file_name = os.path.basename(file_path)
                file_info = {
                    'path': file_path,
                    'name': file_name,
                }
                file_list.append(file_info)

            return Response(file_list)
        else:

            return Response({'error': 'No files found for the unique code'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class FileDownloadDetailView(APIView):
    def get(self, request, unique_code, file_name, format=None):
        delete_expired_files()
        try:
            file = FileModel.objects.get(
                unique_code=unique_code, file__endswith=file_name)
        except FileModel.DoesNotExist:
            return Response({'error': 'File not found'})

        file_path = file.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
