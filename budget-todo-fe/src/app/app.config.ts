import { APP_INITIALIZER, ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
// import { initializeKeycloak } from './keycloak/keycloak.init';
// import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { provideAuth0 } from '@auth0/auth0-angular';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    // KeycloakAngularModule,
    // KeycloakService,
    // {
    //   provide: APP_INITIALIZER,
    //   useFactory: initializeKeycloak,
    //   multi: true,
    //   deps: [KeycloakService]
    // }, 
    provideAuth0(),
    provideAnimationsAsync(), 
    provideAnimationsAsync()
  ]
};
