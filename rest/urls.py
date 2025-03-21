"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MockItemViewSet
# from .views import list_employees,retrieve_employee,create_employee,update_employee,destroy_employee
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register(r'employees', MockItemViewSet, basename='mockitem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), #This is for class
    # path('employees/', list_employees, name='list_employees'),
    # path('employees/<int:pk>/', retrieve_employee, name='retrieve_employee'),
    # path('employees/create/', create_employee, name='create_employee'),
    # path('employees/update/<int:pk>/', update_employee, name='update_employee'),
    # path('employees/delete/<int:pk>/', destroy_employee, name='destroy_employee'),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())

]
