import { Routes } from '@angular/router';
import { NotFoundComponent } from './components/pages/not-found-component/not-found-component';
import { HomeComponent } from './components/pages/home-component/home-component';
import { MonitorPage } from './components/pages/monitor-page/monitor-page';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'monitors', component: MonitorPage },
  // { path: 'logs' },
  // { path: 'settings' },
  // { path: 'notifications' },
  { path: '**', component: NotFoundComponent },
];
