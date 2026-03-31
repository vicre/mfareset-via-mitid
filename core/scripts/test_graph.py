from pprint import pprint

from core.utils.graph import print_hello_world, list_user_authentication_methods


def run(*args):

    upn = args[0] if args else "testtes@dtu.dk"
    print(f"Looking up authentication methods for: {upn}")

    methods = list_user_authentication_methods(upn)

    print("Returned methods:")
    pprint(methods)