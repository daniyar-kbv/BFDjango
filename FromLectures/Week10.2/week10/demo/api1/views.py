from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from main2.models import Student


def index(request):
    data = {
        'hello': True,
        'todos': [
            {
                'id': 1,
                'name': 'todo 1'
            },
            {
                'id': 2,
                'name': 'todo 2'
            }
        ]
    }
    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')


def index2(request):
    data = {
            'hello': True,
            'todos': [
                {
                    'id': 1,
                    'name': 'todo 1'
                },
                {
                    'id': 2,
                    'name': 'todo 2'
                }
            ]
        }
    return JsonResponse(data)


@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students = [s.to_json() for s in students]
        # data = {
        #     'students': students,
        #     'arr': [1, 2, 3]
        # }
        return JsonResponse(students, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        student = Student(name=data['name'], created_by=User.objects.first())
        student.save()
        return JsonResponse(student.to_json())


@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(student.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        student.name = data.get('name', student.name)
        student.save()
        return JsonResponse(student.to_json())
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'deleted': True}, status=204)



