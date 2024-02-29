

from django.http import JsonResponse
from ninja import NinjaAPI

from menu.models import MenuModel

api = NinjaAPI()


@api.get('/')
def get_menu(request, limit: int = 10, offset: int = 0):
    menus = MenuModel.objects.all()[offset:offset + limit]
    serialized_menus = [{'id': menu.id, 'name': menu.name} for menu in menus]
    return JsonResponse(status=200, data={'menus': serialized_menus})
