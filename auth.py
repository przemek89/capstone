import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'coffe-shop-fsnd.eu.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee_shop'

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header

def get_token_auth_header():
    header = request.headers.get('Authorization', None)
    if not header:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is missing'
        }, 401)

    header_split = header.split()

    if len(header_split) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found'
        }, 401)

    elif len(header_split) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    elif header_split[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start with Bearer.'
        }, 401)

    JWT = header_split[1]
    return JWT


def check_permissions(permission, payload):
    if 'permission' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permission not found in JWT'
        }, 400)

    if permission not in payload['permission']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found'
        }, 403)

    return True


def verify_decode_jwt(token):
    url = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks_json = json.loads(url.read())
    header = jwt.get_unverified_header(token)

    if 'kid' not in header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    key = {}
    for key in jwks_json['keys']:
        if key['kid'] == header['kid']:
            key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    if key:
        try:
            payload = jwt.decode(
                token,
                key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. ' +
                            'Please, check the audience and issuer.'
                            }, 401)

        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)

    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            try:
                payload = verify_decode_jwt(token)
            except Exception:
                raise AuthError({
                    'code': 'invalid_token',
                    'description': 'Access denied due to invalid token'
                }, 401)

            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
