import { Routes } from '@angular/router';
import {LoginComponent} from './features/auth/login/login.component';
import {RegisterComponent} from './features/auth/register/register.component';
import {HomeComponent} from './features/home/home.component';
import {FriendAllComponent} from './features/friends/friend-all/friend-all.component';
import {MessagingComponent} from './features/messaging/messaging.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  {path: 'friends', component: FriendAllComponent},
  {path: 'messaging', component: MessagingComponent}
];
