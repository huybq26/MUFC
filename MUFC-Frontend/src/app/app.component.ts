import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {NavigationComponent} from './navigation/navigation.component';
import {VerticalNavigationComponent} from './vertical-navigation/vertical-navigation.component';
import {CoreComponent} from './core/core.component';

@Component({
  selector: 'app-root',
  imports: [CoreComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'MUFC-Frontend';
}
