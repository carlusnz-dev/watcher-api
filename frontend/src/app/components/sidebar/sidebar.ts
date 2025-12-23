import { NgIcon, provideIcons } from '@ng-icons/core';
import { heroHome, heroTv } from '@ng-icons/heroicons/outline';
import { heroHomeSolid, heroTvSolid } from '@ng-icons/heroicons/solid';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-sidebar',
  imports: [RouterLink, NgIcon],
  templateUrl: './sidebar.html',
  styleUrl: './sidebar.css',
  providers: [provideIcons({ heroHome, heroTv, heroHomeSolid, heroTvSolid })],
})
export class Sidebar {
  public sideBarLinks = [
    { id: 1, name: 'Home', path: '/' },
    { id: 2, name: 'Monitors', path: '/monitors' },
    { id: 3, name: 'Logs', path: '/logs' },
    { id: 4, name: 'About', path: '/about' },
    { id: 5, name: 'Settings', path: '/settings' },
    { id: 6, name: 'Notifications', path: '/notifications' },
  ];
}
