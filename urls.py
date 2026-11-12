from django.contrib import admin
from django.urls import path
from djangoapp import views
urlpatterns=[
 path('admin/',admin.site.urls),path('',views.home,name='home'),
 path('about/',views.about,name='about'),path('contact/',views.contact,name='contact'),
 path('dealers/<int:dealer_id>/',views.dealer_detail,name='dealer_detail'),
 path('dealers/state/<str:state>/',views.home,name='by_state'),
 path('postreview/<int:dealer_id>/',views.post_review,name='post_review'),
 path('djangoapp/register',views.register_user),path('djangoapp/login',views.login_user),
 path('djangoapp/logout',views.logout_user),path('djangoapp/get_cars',views.get_cars),
]
