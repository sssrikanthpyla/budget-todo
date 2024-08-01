import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SharedModule } from './shared/shared.module';
import { HeaderComponent } from './shared/header/header.component';
import { AuthService } from '@auth0/auth0-angular';
import { CommonModule } from '@angular/common';
import { DashboardComponent } from './dashboard/dashboard.component';
import { GlobalServiceService } from './global/service/global-service.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    SharedModule,
    HeaderComponent,
    CommonModule,
    DashboardComponent,
    HttpClientModule
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'budget-todo-fe';
  isAuthenticated = false;

  constructor(
    public auth: AuthService,
    private gService: GlobalServiceService
  ) {}

  ngOnInit(): void {
    this.checkAuthentication();
  }

  private async checkAuthentication(): Promise<void> {
    try {
      this.auth.isAuthenticated$.subscribe((isAuthenticated: boolean) => {
        if (isAuthenticated) {
          this.isAuthenticated = true;
          this.getAccessToken();
          this.getCardsDetails();
        }
      });
    } catch (error) {
      console.error('Error during authentication check:', error);
    }
  }

  private async getAccessToken(): Promise<void> {
    try {
      this.auth.idTokenClaims$.subscribe((idTokenClaims: any) => {
        console.log('Inside getAccessTokenWithPopup', idTokenClaims);
      });
    } catch (error) {
      console.error('Error while getting access token:', error);
    }
  }

  private async getCardsDetails(): Promise<void> {
    try {
      this.gService.getCardDetails().subscribe((cardDetails: any) => {
        console.log('Inside getCardDetails', cardDetails);
      });
    } catch (error) {
      console.error('Error while getting card details:', error);
    }
  }

  logInLogOutStatus(event: string): void {
    try {
      if (event === 'login') {
        this.auth.loginWithRedirect();
        this.checkAuthentication();
      } else if (event === 'logout') {
        this.isAuthenticated = false;
        this.auth.logout({ logoutParams: { returnTo: window.location.origin } });
      }
    } catch (error) {
      console.error('Error during login/logout:', error);
    }
  }
}
