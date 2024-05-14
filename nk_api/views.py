from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework import generics, permissions
from .serializers import APiSerializer, ArtSerializer

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
    