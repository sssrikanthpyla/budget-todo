import { APP_INITIALIZER, ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideAuth0 } from '@auth0/auth0-angular';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { HTTP_INTERCEPTORS, provideHttpClient, withInterceptors } from '@angular/common/http';
import { environment } from '../environments/envronment';
import { authInterceptor } from './interceptors/auth.interceptor';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideAuth0(
      {
      domain: environment.authDomain,
      clientId: environment.authClientId,
      authorizationParams: {
        audience: environment.authAudience,
        redirect_uri: window.location.origin
      }
    }
    ),
    provideHttpClient(
      withInterceptors([authInterceptor]),
    ),
    provideAnimationsAsync(), 
    provideAnimationsAsync()
  ]
};
