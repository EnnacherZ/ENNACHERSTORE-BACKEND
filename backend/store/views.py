from django.shortcuts import render
from django.utils.encoding import smart_str
import time
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from rest_framework import status
from .serializers import *
import json

# Create your views here.

ALLOWED_ORIGINS = [
    'http://localhost:3000/',
    'http://192.168.1.110:3000/',
]

@api_view(['GET'])
def get_shoes(request):
    try:
        shoes = Shoe.objects.all()
        serializer = ShoeSerializer(shoes, many=True)
        return Response({'list_shoes': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_newest_shoes(request):
    try:
        newest_shoes = Shoe.objects.filter(newest=True)
        serializer = ShoeSerializer(newest_shoes, many=True)
        return Response({'list_newest_shoes': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_shoes_sizes(request):
    try:
        shoes_sizes = ShoeDetail.objects.all()
        serializer = ShoeDetailSerializer(shoes_sizes, many =True)
        return JsonResponse({'list_shoeSizes':serializer.data}, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return JsonResponse({'message':f'An error occured: {str(e)}'}, status=status.HTTP_401_UNAUTHORIZED)


api_view
@api_view(['POST'])
def test(request):
    try:
        if request.method == 'POST':
            data = request.POST.get('data')
            if data:
                data = json.loads(data)
            new_shoe = Shoe(
                category = data.get('category'),
                ref = data.get('ref'),
                name = data.get('name'),
                price = float(data.get('price')),
                promo = float(data.get('promo')),
                newest = bool(data.get('newest', False)),
                image = request.FILES.get('image')
            )
            new_shoe.save()
            return JsonResponse({'message': 'Shoe uploaded successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({'message': f'An error occured: {str(e)}'}, status=status.HTTP_401_UNAUTHORIZED)



def event_stream_shoes():
    while True:
        shoes = Shoe.objects.all()
        serializer = ShoeSerializer(shoes, many=True)
        data = json.dumps({'list_shoes': serializer.data})
        yield f"data: {smart_str(data)}\n\n"
        time.sleep(2)  # Adjust the frequency of updates as needed

def sse_shoes(request):
        response = StreamingHttpResponse(event_stream_shoes(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        origin = request.headers.get('Origin')
        if origin in ALLOWED_ORIGINS:
            response['Access-Control-Allow-Origin'] = origin  # Adjust as necessary
        return response


def event_stream_shoe_sizes():
    while True:
        shoe_sizes = ShoeDetail.objects.all()
        serializer = ShoeDetailSerializer(shoe_sizes, many=True)
        data = json.dumps({'list_shoeSizes': serializer.data})
        yield f"data: {smart_str(data)}\n\n"
        time.sleep(2)  # Adjust the frequency of updates as needed

def sse_shoe_sizes(request):
        response = StreamingHttpResponse(event_stream_shoe_sizes(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        origin = request.headers.get('Origin')
        if origin in ALLOWED_ORIGINS:
            response['Access-Control-Allow-Origin'] = origin  # Adjust as necessary
        return response
def event_stream_newest_shoe():
    while True:
        shoes = Shoe.objects.filter(newest = True)
        serializer = ShoeSerializer(shoes, many=True)
        data = json.dumps({'list_newest_shoes':serializer.data})
        yield f"data: {smart_str(data)}\n\n"
        time.sleep(2)

def sse_stream_newest_shoes(request):
    response = StreamingHttpResponse(event_stream_newest_shoe(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    origin = request.headers.get('Origin')
    if origin in ALLOWED_ORIGINS:
        response['Access-Control-Allow-Origin'] = origin  # Adjust as necessary
    return response