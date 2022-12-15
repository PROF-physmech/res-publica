from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Authentication service",
      default_version="0.0.1",
      description="Сервис аутенитификации",
   ),
   public=True,
)
