from django.urls import path
from favs.views import resolve_add, favs_see

app_name = "favs"

urlpatterns = [
    path("toggle/<int:pk>/", resolve_add, name="add"),
    path("see/", favs_see, name="see"),
]
