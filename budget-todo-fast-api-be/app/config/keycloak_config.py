# Keycloak configuration
KEYCLOAK_SERVER_URL = "http://keycloak:8080/auth/"
KEYCLOAK_REALM = "budget-todo-realm"
KEYCLOAK_CLIENT_ID = "budget-todo-be-client"
KEYCLOAK_CLIENT_SECRET = "7JpyVBQrTuhlKAPyJE4Tkge7PT7Jmdwn"
KEYCLOAK_OPENID_CONFIG = f"{KEYCLOAK_SERVER_URL}realms/{KEYCLOAK_REALM}/.well-known/openid-configuration"