import {Component, OnInit} from '@angular/core';
import {MatToolbar} from '@angular/material/toolbar';
import {MatAnchor} from '@angular/material/button';
import {NavigationEnd, Router, RouterLink} from '@angular/router';

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
export class NavigationComponent implements OnInit {
  activeLink: string = '/overview';

  constructor(private router: Router) {}

  ngOnInit(): void {
    // Update active link based on current route
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.activeLink = event.urlAfterRedirects;
      }
    });
  }

  setActive(link: string): void {
    this.activeLink = link;
  }
}
