from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_profile, name='search'),
    path('account/', include('django.contrib.auth.urls')),
#     path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
#     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
#     path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password')
]