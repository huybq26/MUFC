import { Component } from '@angular/core';
import {MatToolbar} from '@angular/material/toolbar';
import {MatAnchor} from '@angular/material/button';
import {RouterLink} from '@angular/router';

@Component({
  selector: 'app-navigation',
  imports: [
    MatToolbar,
    MatAnchor,
    RouterLink
  ],
  templateUrl: './navigation.component.html',
  styleUrl: './navigation.component.css'
})
export class NavigationComponent {

}
