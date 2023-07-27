from django.urls import path
from . import views
app_name="shopcart"
urlpatterns = [
    path("",views.allProCart,name="allProCat"),
    path("<slug:c_slug>/",views.allProCart,name="product_by_category"),
    path("<slug:c_slug>/<slug:product_slug>/", views.proDetail, name="proCatetil")

]
