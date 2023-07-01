from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # SIGNUP STUDENT

    path("accounts/signup/student", views.signup_student, name="signup_student"),

    # SIGNUP MERCHANT

    path("accounts/signup/merchant", views.signup_merchant, name="signup_merchant"),

    # LOGIN

    path("accounts/login", views.login, name="login"),


    path("accounts/logout", views.logout, name="logout"),

    # SIGNUP CHOICE

    path("accounts/choose", views.choose_sign_student_merchant, name="choose_sign_student_merchant"),

    # DASHBOARD STUDENT

    path("dashboard/s/", views.dashboard_student, name="dashboard_student"),

    # DASHBOARD MERCHANT

    path("dashboard/m/", views.dashboard_merchant, name="dashboard_merchant"),

    # GET USER DATA
    path("get_user_data", views.get_user_data, name="get_user_data"),


    # FORGOT PASSWORD ROUTE
    path("accounts/password/reset", auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"), name="password_reset"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('accounts/password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('accounts/password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path("accounts/password_reset", auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"), name="password_reset"),



    path("404", views.http404, name="404")

]