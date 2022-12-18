from django.urls import path, include

from .views import schema_view

urlpatterns = [
    path('docs', schema_view.with_ui('swagger')),
    path('login/', include([
        path('admin', AdminLogin.as_view()),
        # path('user', ),
    ])),
    # path('utilize/', include([
    #     path('create/', include([
    #         path('adminCredentials', ),
    #         path('userQr', ),
    #     ])),
    #     path('reset/', include([
    #         path('adminPassword', ),
    #         path('userQr', ),
    #     ])),
    # ]))
]
