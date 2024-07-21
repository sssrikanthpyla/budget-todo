import { Routes } from '@angular/router';
import { HomeModule } from './home/home.module';
import { AuthGuard } from './keycloak/keycloak.guard';
import { CreditcardsModule } from './creditcards/creditcards.module';

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'home',
        pathMatch: 'full'
    },
    {
        path: 'home',
        loadChildren : () => import('./home/home.module').then(m => HomeModule)//, canActivate: [AuthGuard]
    },
    {
        path: 'creditcards',
        loadChildren : () => import('./creditcards/creditcards.module').then(m => CreditcardsModule)//, canActivate: [AuthGuard]
    }
];
