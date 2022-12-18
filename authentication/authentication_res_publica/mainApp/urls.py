from django.urls import path, include

from .views.auth_views import AdminLogin
from .views.doc_view import schema_view

urlpatterns = [
    path('docs', schema_view.with_ui('swagger')),
    path('login/', include([
        path('admin', AdminLogin.as_view()),
        # path('user', ),
    ])),
    # path('utilize/', include([
    #     path('set/', include([
    #         path('adminPassword', ),
    #         path('userQr', ),
    #     ])),
    # ]))
]
