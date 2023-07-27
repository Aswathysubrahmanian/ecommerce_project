# from . models import Category
# def menu_links(request):
#     links=Category.objects.all()
#     context={'links':links}
#     return context


from .models import Category
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)