from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Redirects to /graphql
    path('graphql/', GraphQLView.as_view(graphiql=True), name="graphiql"),
]
