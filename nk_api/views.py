from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework import generics, permissions
from .serializers import APiSerializer, ArtSerializer, UserDataSerializer

from . models import Api, Art

# Create your views here.

from django.http import HttpResponse

class RecordUpdateApi(generics.UpdateAPIView):
    queryset = Api.objects.all()
    serializer_class = APiSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['put']
      

class RecordCreatedApi(generics.CreateAPIView):
    queryset = Api.objects.all()
    serializer_class = APiSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class LISTAPI(generics.ListAPIView):
    queryset = Api.objects.all()
    serializer_class = APiSerializer
    http_method_names = ['get']

####### ART #############
    
class ArtGet(generics.ListAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    http_method_names = ['get']    

class ArtPost(generics.CreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def api_html(request):
	if request.user.is_authenticated:
		#See the records
		api = Api.objects.all()
		return render(request,'api_html.html',{'api':api})
	else:
		messages.error(request, 'You Must Be Authenticated To Access Here!...')
		return redirect('saludo')


'''
Esta funcion importa el modulo connection para crear un cursor 
y trabajar directamente con la base de datos. 

'''
from django.db import connection
     
def store_proc(request):
    cursor = connection.cursor()
    query = 'SELECT nombre, email FROM nk_tb_crmAPI;'
    with connection.cursor() as cursor:
        cursor.execute(query)
        api = cursor.fetchall()
        for row in api:
            print(row[0],' ' ,row[1]) 
    return render(request, 'store_proc.html', {'api':api} )

def create_store_get_users(request):
     '''
     Esta funcion crea un STORE PROCEDURE que selecciona todos los campos de la 
     BD nk_tb_crmAPI. (Los SP no pueden tener un parentesis en el nombre sino da error).
     Este SP se guarda en la BD con el nombre get_users. Si el SP se crea devuelve un mensaje de exito. 
     '''
     cursor = connection.cursor()
     proc = '''
            create procedure get_users__
            As
            SELECT * FROM nk_tb_crmAPI
            go;
            '''
     with connection.cursor() as cursor:
          if cursor.execute(proc): message = 'Store procedure creado correctamente'
          else:
               message = 'Sucedio un error en la creacion del Store procedure get_users'
     return render(request, 'create_store_get_users.html', {'message':message} )

def get_proc_users(request):
    '''
    Esta funcion ejecuta el SP get_users y lo pasa a una variable para mostar el contenido
    en la pagina web. 
    '''
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute('EXEC get_users')
        results = cursor.fetchall()
    return render(request, 'get_proc_users.html', {'results':results} )
    

###### Learning from book Django_RESTful_Web_Services_The_Easiest_Way_to_Bui...
    
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from nk_api.models import Api
from nk_api.serializers import UserDataSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = Api.objects.all()
        uses_serializer = UserDataSerializer(users, many=True)
        return JSONResponse(uses_serializer.data)
    elif request.method == 'POST':
        print(request.data)
        user_data = JSONParser().parse(request)
        user_serializer = UserDataSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data, \
            status=status.HTTP_201_CREATED)
        return JSONResponse(user_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def user_detail(request, pk):
    try:
        user = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserDataSerializer(user) 
        if user:
            return JSONResponse(user_serializer.data)
        else:
            messages.error(request, 'This user dont exist!...')
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserDataSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data)
        return JSONResponse(user_serializer.errors, \
                status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


'''
Esta es la forma correcta indicada por la documentacion
'''
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    Muestra todos los usuarios y permite crear usuarios.
    """
    if request.method == 'GET':
        users = Api.objects.all()
        serializer = UserDataSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete an user.
    """
   
    try:
        user = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDataSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)