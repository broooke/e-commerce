from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('view/<str:name>/', views.detailView, name='detail'),
    path('signup/', views.SignUpView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('order/', views.orderView, name='order'),
    path('order/add/<str:name>/', views.add_order, name='add'),
    path('order/<str:name>/add_quantity/', views.addQuantityView,name='add_quantity'),
    path('order/<str:name>/less_quantity/', views.lessQuantityView,name='less_quantity'),
    path('checkout/', views.checkoutView, name='checkout'),
]