import { Component, EventEmitter, Inject, Input, Output } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatMenuModule, MatMenuPanel} from '@angular/material/menu';
import {RouterModule} from '@angular/router';
import { AuthService } from '@auth0/auth0-angular';
import { CommonModule, DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MatToolbarModule, MatButtonModule, MatIconModule, MatMenuModule, RouterModule, CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  accounts!: MatMenuPanel<any>;

  // isUserLoggedIn!: boolean;

  constructor(
    public authService: AuthService,
    @Inject(DOCUMENT) public document: Document
  ) {}

  // login() {
  //   this.authService.loginWithRedirect();
  //   this.isUserLoggedIn = true;
  // }
  
  // signOut() {
  //   this.authService.logout({ logoutParams: { returnTo: window.location.origin } });
  //   this.isUserLoggedIn = false;
  // }
  
}
