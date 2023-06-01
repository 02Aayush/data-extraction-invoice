from django.urls import path
from . import views
# from .api_views import hello_world
from .api_views import invoice_data_list

urlpatterns = [
    path('', views.login_view, name='login'),

    path('accounts/login/', views.login_view, name='login'),

    path('signup/', views.signup_view, name='signup'),

    path('logout/', views.logout_view, name='logout'),

    path('upload-invoice/', views.upload_invoice, name='upload_invoice'),

    path('process_invoice', views.upload_invoice, name='process_invoice'),

    path('invoice-list/', views.invoice_details, name='invoice_list'),

    path('download-csv/<str:csv_file_path>/', views.download_csv, name='download_csv'),

    # path('api/hello/', hello_world, name='api_hello'), sample api testing

    path('api/invoices/', invoice_data_list, name='api_invoice_data_list'),
]