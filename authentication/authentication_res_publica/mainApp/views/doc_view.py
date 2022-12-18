from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from ..utils.swagger_generator import CustomOpenAPISchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication service",
        default_version="0.0.1",
        description="Сервис аутенитификации",
    ),
    public=True,
    generator_class=CustomOpenAPISchemaGenerator,
)
