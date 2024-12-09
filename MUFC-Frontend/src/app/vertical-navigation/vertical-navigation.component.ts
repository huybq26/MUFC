import {Component, EventEmitter, Input, Output} from '@angular/core';
import {MatSidenav, MatSidenavContainer} from '@angular/material/sidenav';
import {MatListItem, MatNavList} from '@angular/material/list';
import {MatIcon} from '@angular/material/icon';
import {RouterLink} from '@angular/router';
import {MatAnchor} from '@angular/material/button';

@Component({
  selector: 'app-vertical-navigation',
  imports: [
    MatSidenavContainer,
    MatNavList,
    MatIcon,
    RouterLink,
    MatSidenav,
    MatAnchor
  ],
  templateUrl: './vertical-navigation.component.html',

  styleUrl: './vertical-navigation.component.css',
})
export class VerticalNavigationComponent {
  // logic to open on click on menu icon
  @Input() openSignal:boolean=false;

}
