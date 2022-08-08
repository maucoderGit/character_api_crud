"""API views file."""
# Django
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
# Local
from .models import Character


class CharacterView(View):
    """Character CRUD class based view."""
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        """HTTP Methods: GET
        
        Returns all the characters stored on database.
        """
        if id != 0:
            characters = list(Character.objects.filter(id=id).values())
            if len(characters) > 0:
                character = characters[0]
                data = {
                    'message': 'Success',
                    'character': character
                }
            else: 
                data = {
                    'message': 'character not found.'
                }
        else:
            characters = list(Character.objects.values())
            if len(characters) > 0:
                data = {
                    'message':'Success',
                    'characters': characters
                }
            else:
                data = {
                    'message':'Characters not found.',
                }
        return JsonResponse(data)


    def post(self, request):
        """Http methods: Post
        
        This method create a character and store them in the database.
        
        Fields:
        - name: str
        - appears_in: str
        """
        jd = json.loads(request.body)
        Character.objects.create(
            name=jd['name'],
            appears_in=jd['appears_in']
        )
        data = {
            'message': 'Success',
        }
        return JsonResponse(data)

    def put(self, request, id):
        """Http methods: Put"""
        jd = json.loads(request.body)
        characters = list(Character.objects.filter(id=id).values())
        if len(characters) > 0:
            character = Character.objects.get(id=id)
            character.name = jd['name']
            character.appears_in = jd['appears_in']
            character.save()
            data = {
                'message': 'Success'
            }
        else:
            data = {
                'message': 'Character not found'
            }
        return JsonResponse(data)

    def remove(self, request):
        """"""
