from django.urls import path
from.import views
# In cadrul acestui fisier vom defini lista de app pointuri a aplicatiei

urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload_product/', views.upload_product, name='upload_product')
]