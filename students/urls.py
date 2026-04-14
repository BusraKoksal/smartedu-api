from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, CourseViewSet

# Router nesnesini oluşturuyoruz

router=DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)

# URL pattern'leri router üzerinden çekiyoruz
urlpatterns = [
    path('', include(router.urls)),
]
