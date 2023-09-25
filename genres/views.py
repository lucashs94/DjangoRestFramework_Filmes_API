import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Genre


@csrf_exempt
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        genre = Genre(name=data['name'])
        genre.save()
        return JsonResponse(
            { 'id': genre.id, 'name': genre.name }, 
            status=201
        )
        
        
@csrf_exempt
def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    
    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name }
        return JsonResponse(data)
        
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            { 'id': genre.id, 'name': genre.name }, 
            status=200
        )
        
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            { 'message': 'Deleted with success' }, 
            status=204
        )