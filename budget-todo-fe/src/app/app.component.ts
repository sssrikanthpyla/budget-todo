import { Component, Inject, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SharedModule } from './shared/shared.module';
import { HeaderComponent } from './shared/header/header.component';
import { AuthService, AuthState } from '@auth0/auth0-angular';
import { CommonModule, DOCUMENT } from '@angular/common';
import { DashboardComponent } from './dashboard/dashboard.component';
import { GlobalServiceService } from './global/service/global-service.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SharedModule, HeaderComponent, CommonModule, DashboardComponent, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit{
  title = 'budget-todo-fe';

  constructor(
    public auth: AuthService,
    private gService: GlobalServiceService
    ) {}

  ngOnInit(): void {
    this.checkAuthentication();
  }

  checkAuthentication() {
    this.auth.isAuthenticated$.subscribe((res: any) => {
      if(res) {
        this.getAccessToken();
        this.getCardsDetails();
      }
    });
  }

  getAccessToken() {
    this.auth.idTokenClaims$.subscribe((res: any) => {
      console.log('Inside getAccessTokenWithPopup');
      console.log(res);
    });
  }

  getCardsDetails() {
    this.gService.getCardDetails().subscribe((res: any) => {
      console.log('Inside getCardDetails');
      console.log(res);
    });
  }
  
}
