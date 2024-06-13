from django.contrib import admin
from django.urls import path, include
from article_feed.views import *
from django.conf import settings
from django.conf.urls.static import static
#import rest_framework.urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

"""
    REST API ENDPOINTS

    Шаблоны url:
       - api/<имя_сущности>/          - Получение списка всех объектов сущности для чтения;
       - api/<имя_сущности>/create/   - Создание объекта сущности админом;
       - api/<имя_сущности>/<int:pk>/ - Редактирование/удаление определенного объекта 
                                        сущности, получаемого по id (pk), админом 
                                        или чтение этого объекта неавторизоавнным пользователем; 
    
    ПРИМЕЧАНИЕ: поведение сущности ОБРАЩЕНИЕ отличается
"""

urlpatterns = [
    path('', index, name='main'),
    path('admin/', admin.site.urls),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Вход и выход, получение/обновление токена
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),    

    #ПОСТЫ БЛОГА И ПРОЕКТОВ
    #Все посты
    path('api/posts/', PostAPIView.as_view()),
    #Посты по категориям
    path('api/posts/blog/', BlogPostsAPIView.as_view()),
    path('api/posts/projects/', ProjectsPostsAPIView.as_view()),

    path('api/posts/create/', PostCreateAPIView.as_view()),
    #Загрузка изображений
    path('api/posts/upload/', PostFileUploadAPIView.as_view()),

    path('api/posts/<int:pk>/', PostUPdateDeleteAPIView.as_view()),

    #ДОКУМЕНТЫ
    path('api/docs/', DocsAPIView.as_view()),
    path('api/docs/create/', DocsCreateAPIView.as_view()),
    path('api/docs/<int:pk>/', DocsUpdateDeleteAPIView.as_view()),

    #ГРУППЫ ОТЧЕТОВ
    path('api/groups/', GroupsAPIView.as_view()),
    path('api/groups/create/', GroupsCreateAPIView.as_view()),
    path('api/groups/<int:pk>/', GroupsUpdateDeleteAPIView.as_view()),
    #ОТЧЕТЫ
    path('api/reports/', ReportsAPIView.as_view()),
    #Получение отчетов в пределах определенной группы
    path('api/groups/reports-in-group/<int:pk>/', ReportsByGroupAPIView.as_view()),
    path('api/reports/create/', ReportsCreateAPIView.as_view()),
    path('api/reports/<int:pk>/', ReportsUpdateDeleteAPIView.as_view()),
    
    #ТОВАРЫ
    path('api/products/', ProductAPIView.as_view()),
    path('api/products/create/', ProductCreateAPIView.as_view()),
    path('api/products/<int:pk>/', ProductUPdateDeleteAPIView.as_view()),

    #FAQ
    path('api/faq/', FAQAPIView.as_view()),
    path('api/faq/create/', FAQCreateAPIView.as_view()),
    path('api/faq/<int:pk>/', FAQUPdateDeleteAPIView.as_view()),

    #ОБРАЩЕНИЯ
    #Любой посетитель может отправить сообщение
    path('api/forms/create/', CreateEmailAPIView.as_view()),
    #Обращения может просматривать только Администратор
    #Обращения предназначены только для ознакомления
    path('api/forms/', DataFromFormsAPIView.as_view()),
    path('api/forms/<int:pk>/', DataFromFormsSingleAPIView.as_view()),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)