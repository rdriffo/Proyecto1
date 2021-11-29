from django.urls    import  path
from app            import  views

urlpatterns = [
    
    path('get_data/', views.get_data.as_view()),
    path('pagina/<int:rut>/', views.retornar_page)
   # path('imagen/', views.get_foto),
    
]