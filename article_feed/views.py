#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


def index(request):
    pass

#Posts
class PostAPIView(generics.ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class PostFileUploadAPIView(generics.CreateAPIView):
   permission_classes = [IsAuthenticated]

   queryset = postContentFilesUpload.objects.all()
   serializer_class = PostFileUpload

class PostCreateAPIView(generics.CreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class BlogPostsAPIView(APIView):
    
    def get(self, request, format=None):
        try:
            filtered_objects = post.objects.filter(category='blog')
            serializer = PostSerializer(filtered_objects, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProjectsPostsAPIView(APIView):
    
    def get(self, request, format=None):
        try:
            filtered_objects = post.objects.filter(category='projects')
            serializer = PostSerializer(filtered_objects, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

#Docs

class DocsAPIView(generics.ListAPIView):
    queryset = docs.objects.all()
    serializer_class = DocsSerializer

class DocsCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        print(request.data)
        serializer = DocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = docs.objects.all()
    serializer_class = DocsSerializer

class ReportsByGroupAPIView(APIView):
    
    def get(self, request, pk, format=None):
        try:
            group = reportsGroup.objects.get(pk=pk)
            filtered_objects = reports.objects.filter(group=group.pk)
            serializer = ReportsSerializer(filtered_objects, many=True)
            return Response(serializer.data)
        except reportsGroup.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class ReportsAPIView(generics.ListAPIView):
    queryset = reports.objects.all()
    serializer_class = ReportsSerializer
class ReportsCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        print(request.data)
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = reports.objects.all()
    serializer_class = ReportsSerializer

class GroupsAPIView(generics.ListAPIView):
    queryset = reportsGroup.objects.all()
    serializer_class = ReportGroupSerializer

class GroupsCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = reportsGroup.objects.all()
    serializer_class = ReportGroupSerializer


class GroupsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = reportsGroup.objects.all()
    serializer_class = ReportGroupSerializer
#FAQ

class FAQAPIView(generics.ListAPIView):
    
    queryset = faq.objects.all()
    serializer_class = FAQSerializer

class FAQCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = faq.objects.all()
    serializer_class = FAQSerializer


class FAQUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly] 

    queryset = faq.objects.all()
    serializer_class = FAQSerializer

#Product

class ProductAPIView(generics.ListAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = products.objects.all()
    serializer_class = ProductSerializer

#Messages from form

from django.core.mail import send_mail, get_connection
from django.conf import settings
class CreateEmailAPIView(APIView):
    def post(self,request):
        print(request.data)
        data=request.data
        serializer = FormsSerializer(data=data)
        if serializer.is_valid():
            try:
                connection = get_connection(
                    host = settings.EMAIL_HOST,
                    port = settings.EMAIL_PORT,
                    username = settings.EMAIL_HOST_USER,
                    password = settings.EMAIL_HOST_PASSWORD,
                    use_ssl = True)
                subject = 'Новое обращение!'
                if data.get("name", None) or data.get("message",None) or data.get("phone",None):
                    message =  f'Имя:{data.get("name", None)} \n \n {data.get("message",None)} \n \n Контакты для связи: \n Email: {data.get("email",None)} \n Телефон: {data.get("phone",None)}'
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    connection = connection,
                    fail_silently=False,)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except: 
                return Response("Ошибка при отправке", status=status.HTTP_400_BAD_REQUEST)   
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataFromFormsAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = dataFromForms.objects.all()
    serializer_class = FormsSerializer


class DataFromFormsSingleAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = dataFromForms.objects.all()
    serializer_class = FormsSerializer


class LoginAPIView(APIView):

    def post(self, request):

        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None or password is None:
            return Response({'error': 'Нужен и логин, и пароль'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Неверные данные'},status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        refresh.payload.update({
            'user_id': user.id,
            'username': user.username
        })
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token') # С клиента нужно отправить refresh token
        if not refresh_token:
            return Response({'error': 'Необходим Refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist() # Добавить его в чёрный список
        except Exception as e:
            return Response({'error': 'Неверный Refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': 'Выход успешен'}, status=status.HTTP_200_OK)

