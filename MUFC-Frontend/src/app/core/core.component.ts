import { Component } from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {VerticalNavigationComponent} from '../vertical-navigation/vertical-navigation.component';
import {NavigationComponent} from '../navigation/navigation.component';

@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  imports: [
    RouterOutlet,
    VerticalNavigationComponent,
    NavigationComponent
  ],
  styleUrls: ['./core.component.css']
})
export class CoreComponent {}
