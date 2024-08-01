import { Component, EventEmitter, Inject, Input, OnChanges, OnInit, Output, SimpleChanges } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatMenuModule, MatMenuPanel} from '@angular/material/menu';
import {RouterModule} from '@angular/router';
import { AuthService } from '@auth0/auth0-angular';
import { CommonModule, DOCUMENT } from '@angular/common';
import {MatFormFieldModule} from '@angular/material/form-field';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MatToolbarModule, MatButtonModule, MatIconModule, MatMenuModule, RouterModule, CommonModule, MatFormFieldModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent  implements OnInit, OnChanges{
  accounts!: MatMenuPanel<any>;
  @Input() isAuthenticated: any;
  @Output() logInLogOutStatus = new EventEmitter<any>();

  isLoggedIn: any;
  
  constructor(
    public authService: AuthService,
    @Inject(DOCUMENT) public document: Document
  ) {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes && changes['isAuthenticated'].currentValue) {
      this.isLoggedIn = changes['isAuthenticated'].currentValue
    }
  }
  ngOnInit(): void {}

  logInLogOut(status: any) {
    this.logInLogOutStatus.emit(status);
  }
  
}
