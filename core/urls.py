from django.urls import path
from stores import views as store_views

app_name = "core"

urlpatterns = [
    path("", store_views.all_stores, name="home")
]