import { Component, EventEmitter, Input, Output } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatMenuModule, MatMenuPanel} from '@angular/material/menu';
import {RouterModule} from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MatToolbarModule, MatButtonModule, MatIconModule, MatMenuModule, RouterModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  accounts!: MatMenuPanel<any>;

  @Input() isUserLoggedIn!: boolean;
  @Output() loginLogout = new EventEmitter<any>();

  login() {
    this.loginLogout.emit('LOGEDIN');
  }

  signOut() {
    this.loginLogout.emit('LOGEDOUT');
  }
}
