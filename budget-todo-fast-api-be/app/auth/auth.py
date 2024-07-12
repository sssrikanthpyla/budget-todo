from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from app.config.keycloak_config import KEYCLOAK_SERVER_URL, KEYCLOAK_REALM, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET
from app.models.user_model import User

# Keycloak configuration
# KEYCLOAK_SERVER_URL = "http://keycloak:8080/auth/"
# KEYCLOAK_REALM = "myrealm"
# KEYCLOAK_CLIENT_ID = "myclient"
# KEYCLOAK_CLIENT_SECRET = "uUglaN5bradPZStwNaXocguvhxfc7BLJ"
# KEYCLOAK_OPENID_CONFIG = f"{KEYCLOAK_SERVER_URL}realms/{KEYCLOAK_REALM}/.well-known/openid-configuration"

keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM,
    client_secret_key=KEYCLOAK_CLIENT_SECRET
)

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{KEYCLOAK_SERVER_URL}realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{KEYCLOAK_SERVER_URL}realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
)

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        userinfo = keycloak_openid.userinfo(token)
        return User(username=userinfo['preferred_username'], email=userinfo['email'])
    except KeycloakAuthenticationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )