from django.urls import path
from calculator.views import home_view,Calendar_view,login_view,logout_view,register_view
#  , classes_view

urlpatterns = [
    path('', home_view , name = 'home'),
    # path('/class', classes_view, name= 'classes')
    path('calendar/', Calendar_view.as_view(), name='calendar'),
    # path('calendar/<str:month>', Calendar_view.as_view(), name="calendar")
    # path('calendar/', calendar_view, name="calendar"),
    # path(r'^calendar/(?P[^/]+)$', calendar_view, name="calendar")
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register')
    

    
]

