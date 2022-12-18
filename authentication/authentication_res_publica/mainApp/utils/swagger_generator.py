from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        """Generate a :class:`.Swagger` object with custom tags"""

        swagger = super().get_schema(request, public)
        swagger.tags = [
            {
                "name": "Authentication",
                "description": "Методы для входа"
            },
            {
                "name": "Administration",
                "description": "Методы администрирования реквизитов входа"
            },
        ]

        return swagger
