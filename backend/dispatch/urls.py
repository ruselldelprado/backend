from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.hero,name="hero"),
    path('dashboard/', views.home, name="dashboard"),
    path('personel/', views.personel),
    path('calls/', views.showView, name="calls"),
    path('calls/form', views.callsFormView, name="calls_form"),
    path('calls/<int:id>', views.updateView, name='update_url'),
    path('calls/del/<int:id>', views.deleteView, name='delete_url'),
    path('dispatcher-report/',views.dispatcher_report)
]
