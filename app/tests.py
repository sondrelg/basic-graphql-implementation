import json

from graphene_django.utils.testing import GraphQLTestCase
from .schema import schema


class MyFancyTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def test_some_query(self):
        response = self.query(
            '''
            {
              users {
                name
                lastName
              }
            }
            ''',
            op_name='users'
        )
        json.loads(response.content)
        self.assertResponseNoErrors(response)
