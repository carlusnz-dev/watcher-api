import { Routes } from '@angular/router';
import { MonitorAll } from './components/monitor-all/monitor-all';
import { NotFound } from './components/notfound/notfound';

export const routes: Routes = [
  { path: '', component: MonitorAll },
  { path: '**', component: NotFound },
];
