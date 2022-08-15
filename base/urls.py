from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, Registro
from django.contrib.auth.views import LogoutView

urlpatterns = [path("", ListaPendientes.as_view(), name="tareas"),
               path("tarea/<int:pk>", DetalleTarea.as_view(), name="tarea"),
               path("crear/", CrearTarea.as_view(), name="crear"),
               path("editar/<int:pk>", EditarTarea.as_view(), name="editar"),
               path("eliminar/<int:pk>", EliminarTarea.as_view(), name="eliminar"),
               path("login/", Logueo.as_view(), name="login"),
               path("logout/", LogoutView.as_view(next_page="tareas"), name="logout"),
               path("registro/", Registro.as_view(), name="registro")]
