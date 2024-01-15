from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
# router.register("todos",views.TodosView,basename="todos")
router.register("todos",views.TodoViewSetView,basename="todos")

urlpatterns = [

    path("register/",views.SignupView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    
]+router.urls