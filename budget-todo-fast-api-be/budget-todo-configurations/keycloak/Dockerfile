FROM quay.io/keycloak/keycloak:23.0.1 as builder
COPY ./themes/budget-todo/ /opt/keycloak/themes/budget-todo/
COPY ./provider/ /opt/keycloak/providers/

FROM quay.io/keycloak/keycloak:23.0.1
COPY --from=builder /opt/keycloak/ /opt/keycloak/
ENV KC_PROXY=passthrough
ENV KEYCLOAK_ADMIN=admin
ENV KEYCLOAK_ADMIN_PASSWORD=admin
ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]