from django.urls import path

from apps.cources.views import CourceListView, CourceDetailView
from apps.users.views import StudentCreateView

urlpatterns = [
    path('student/create', StudentCreateView.as_view(), name='student-create'),
]