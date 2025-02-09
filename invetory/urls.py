from django .urls import path
from.import views

urlpatterns=[
    path('',views.home, name='home'),
     path('register',views.register, name='register'),
     path('login',views.login_user,name='login'),
    path('index',views.index, name='index'),
    path('logout',views.logout_user, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('add',views.add_record, name='add'),
    path('update/<int:pk>',views.update_inventory, name='update'),
    path('delete/<int:pk>',views.delete_record, name='delete'),
    path('about',views.about, name='about'),
    path('service',views.service, name='service'),
    path('contact',views.contact, name='contact')
]
