from cas import CASClient
from utils import get_profile_route_name, get_host_url


def get_auth_client():
    return CASClient(
        version=3,
        service_url=f"http://{get_host_url()}/login?next={get_profile_route_name()}",
        server_url="https://django-cas-ng-demo-server.herokuapp.com/cas/",
    )