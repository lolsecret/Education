from django.urls import path

from apps.cources.views import CourceListView, CourceDetailView

urlpatterns = [
    path('', CourceListView.as_view(), name='cources-list'),
    path('<int:pk>', CourceDetailView.as_view(), name='cource-detail'),
]