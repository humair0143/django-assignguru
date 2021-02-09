from django.urls import path


from accounts.views import (
    login_view,
    logout_view,
    register_view,
)

from django.views.generic import TemplateView

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
