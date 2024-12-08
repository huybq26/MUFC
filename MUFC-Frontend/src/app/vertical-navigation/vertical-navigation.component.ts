import { Component } from '@angular/core';
import {MatSidenav, MatSidenavContainer} from '@angular/material/sidenav';
import {MatListItem, MatNavList} from '@angular/material/list';
import {MatIcon} from '@angular/material/icon';
import {RouterLink} from '@angular/router';

@Component({
  selector: 'app-vertical-navigation',
  imports: [
    MatSidenavContainer,
    MatNavList,
    MatListItem,
    MatIcon,
    RouterLink,
    MatSidenav
  ],
  templateUrl: './vertical-navigation.component.html',
  styleUrl: './vertical-navigation.component.css'
})
export class VerticalNavigationComponent {

}
