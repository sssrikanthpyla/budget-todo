import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SharedModule } from './shared/shared.module';
import { HeaderComponent } from './shared/header/header.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SharedModule, HeaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'budget-todo-fe';

  isUserLoggedIn: boolean = false;

  checkLoginLogout(event: any) {
    if(event === 'LOGEDIN') {
      this.isUserLoggedIn = true;
    }
    if(event === 'LOGEDOUT') {
      this.isUserLoggedIn = false;
    }
  }
}
