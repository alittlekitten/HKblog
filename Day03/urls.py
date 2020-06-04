from django.contrib import admin
from django.urls import path
import myapp.views # 해줘야 아래에서 쓸 수 있는것!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="index"),
    path('myapp/create',myapp.views.create, name="create"), # 앞의 create는 view의 create고 뒤는 html의 create이다.
    path('myapp/create_pro', myapp.views.create_pro, name="create_pro"),#마찬가지 단 createpro는 안보이는 페이지기떄문에 html안만든거 create연계 db에 create페이지에서 넣은거 넣어주기 위한
    path('myapp/show', myapp.views.show, name="show"),
    path('myapp/updateSearch', myapp.views.updateSearch, name="updateSearch"),
    path('myapp/search', myapp.views.search, name="search"),
    path('myapp/update', myapp.views.update, name="update"),
    path('myapp/deleteSearch', myapp.views.deleteSearch, name="deleteSearch"),
    path('myapp/find', myapp.views.find, name="find"),
    path('myapp/delete', myapp.views.delete, name="delete")
]
