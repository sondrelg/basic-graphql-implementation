from django.shortcuts import redirect


def index(request):
    """
    Redirects to /graphql
    """
    return redirect('graphiql')
