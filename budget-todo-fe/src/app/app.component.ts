import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SharedModule } from './shared/shared.module';
import { HeaderComponent } from './shared/header/header.component';
import { _KeycloakService } from './keycloak/keycloak.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SharedModule, HeaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit{
  title = 'budget-todo-fe';
  isUserLoggedIn: boolean = false;
  userDetails: any = {};

  constructor(private _keyclockService: _KeycloakService) {}

  ngOnInit(): void {
      this.getUserDetals();
  }

  getUserDetals() {
    this.userDetails['userName'] = this._keyclockService.getUsername();
  }

  checkLoginLogout(event: any) {
    if(event === 'LOGEDIN') {
      this.isUserLoggedIn = true;
    } else if(event === 'LOGEDOUT') {
      this._keyclockService.logout()
      this.isUserLoggedIn = false;
    }
  }
}
