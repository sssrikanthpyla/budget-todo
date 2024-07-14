import { Injectable } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';

@Injectable({
    providedIn: 'root'
  })
export class _KeycloakService{
    constructor(private keycloak: KeycloakService) {}

    login(): void {
        this.keycloak.login();
    }

    isLogedin() {
        return this.keycloak.isLoggedIn();
    }

    getUsername() {
        return this.keycloak.getUsername();
    }

    logout(): void {
        this.keycloak.logout();
    }
}