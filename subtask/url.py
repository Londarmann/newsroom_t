
from ninja import NinjaAPI

from subtask.models import SubTask

api = NinjaAPI()

from django.http import JsonResponse

@api.get('/')
def get_menu(request,):
    tasks = SubTask.objects.all()
    serialized_menus = [{'id': task.id, 'title': task.title,
                         'description': task.description, 'time': task.finished_time} for task in tasks]
    return JsonResponse(status=200, data={'menus': serialized_menus})
