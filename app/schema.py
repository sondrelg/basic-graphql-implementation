import graphene
from graphene_django import DjangoObjectType

from .models import UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()


schema = graphene.Schema(query=Query)
