import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Sidebar } from './components/sidebar/sidebar';
import { MonitorAll } from './components/monitor-all/monitor-all';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Sidebar, MonitorAll],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected readonly title = signal('frontend');
}
