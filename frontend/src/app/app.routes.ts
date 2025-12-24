import { Routes } from '@angular/router';
import { NotFoundComponent } from './components/pages/not-found-component/not-found-component';
import { HomeComponent } from './components/pages/home-component/home-component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  // { path: 'monitors' },
  // { path: 'logs' },
  // { path: 'settings' },
  // { path: 'notifications' },
  { path: '**', component: NotFoundComponent },
];
