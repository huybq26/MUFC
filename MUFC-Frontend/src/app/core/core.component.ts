import { Component } from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {VerticalNavigationComponent} from './components/vertical-navigation/vertical-navigation.component';
import {NavigationComponent} from './components/navigation/navigation.component';
import {MatIcon} from '@angular/material/icon';
import {MatIconButton} from '@angular/material/button';

@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  imports: [
    RouterOutlet,
    // VerticalNavigationComponent,
    NavigationComponent,
    MatIcon,
    MatIconButton
  ],
  styleUrls: ['./core.component.css']
})
export class CoreComponent {
  openSignalInput: boolean = false;

  toggleOpenSignalInput(): void {
    this.openSignalInput = !this.openSignalInput;
  }
}
