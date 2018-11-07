from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main2.models import Student
from api2.serializers import StudentSerializer, StudentModelSerializer
import json


@csrf_exempt
def students_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = StudentModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})


@csrf_exempt
def students_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        serializer = StudentModelSerializer(student)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = StudentModelSerializer(instance=student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'deleted': True})


