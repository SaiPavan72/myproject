from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path('register/',views.register, name='register'),
    path('login_success_or_not/',views.login_success_or_not, name='login_success_or_not'),
    path('show/', views.show, name='show.html'),
    path('<int:recipe_id>/',views.details, name='details.html'),
    path('create_recipe/',views.create_page,name='create_recipe'),
    path('save_recipe/', views.save_recipe, name='save_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('logout/',views.logout_page, name='logout'),
    path('save/',views.save_details,name='save')
]
