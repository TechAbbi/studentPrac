from django.urls import path, include
from rest_framework import routers
from . views import StudentView, SubjectView, SubjectEntryView, student_result_view
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register("student", StudentView)
router.register("subject", SubjectView)
router.register("marks", SubjectEntryView)

urlpatterns = [
    path("api/", include(router.urls)),
    path('student_result/<int:student_id>/', student_result_view, name='student_result'),
    path("auth_token/", obtain_auth_token, name="auth_token"),
]



