from django.urls import path
from .views import home,all, search_results, category_view,about,contact

urlpatterns = [
    path("", home, name="home_page"),
    path('products/', all, name='all_products'),
    path('search/', search_results, name='search_results'),
    path('category/<int:category_id>/', category_view, name='category_view'),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    
]