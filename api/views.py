from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import *
from django.http import Http404

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'Meme List':'https://crio-xmeme.herokuapp.com/api/memes/',
        'Single Meme':'https://crio-xmeme.herokuapp.com/api/memes/<str:pk>',
        'Meme Post':'https://crio-xmeme.herokuapp.com/api/memes-create/',
        'Meme Post Delete' :'https://crio-xmeme.herokuapp.com/api/memes-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    try:
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)
    except Task.DoesNotExist:
        raise Http404("User does not exist")

@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    return Response("Item Deleted Sucessfully")
