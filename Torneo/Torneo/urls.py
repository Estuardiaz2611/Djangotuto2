from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, logout_then_login,\
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('liga/', include (('apps.liga.urls', 'liga'), namespace='liga')),
    path('equipo/', include (('apps.equipo.urls', 'equipo'), namespace='equipo')),
    path('usuario/', include (('apps.usuario.urls', 'usuario'), namespace='usuario')),
    path('accounts/login/', LoginView.as_view(template_name='inde.html'), name="login"),
    path('logout/', logout_then_login, name="logout"),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html', 
            email_template_name='registration/password_reset_email.html'), name="password_reset"),

    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
            name="password_reset_done"),

    path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
            name="password_reset_confirm"),

    path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
            name="password_reset_complete"),
]