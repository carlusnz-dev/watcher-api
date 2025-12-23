import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { provideIcons, NgIcon } from '@ng-icons/core';
import {
  heroBell,
  heroCog6Tooth,
  heroHome,
  heroInformationCircle,
  heroTv,
} from '@ng-icons/heroicons/outline';
import {
  heroBellSolid,
  heroCog6ToothSolid,
  heroHomeSolid,
  heroInformationCircleSolid,
  heroTvSolid,
} from '@ng-icons/heroicons/solid';

@Component({
  selector: 'app-sidebar-component',
  imports: [RouterLink, NgIcon, RouterLinkActive],
  templateUrl: './sidebar-component.html',
  styleUrl: './sidebar-component.css',
  providers: [
    provideIcons({
      heroHome,
      heroHomeSolid,
      heroTv,
      heroTvSolid,
      heroInformationCircle,
      heroInformationCircleSolid,
      heroCog6Tooth,
      heroCog6ToothSolid,
      heroBell,
      heroBellSolid,
    }),
  ],
})
export class SidebarComponent {
  public navLinks = [
    { id: 1, name: 'Home', path: '', icon: 'heroHome' },
    { id: 2, name: 'Monitor', path: 'monitors', icon: 'heroTv' },
    { id: 3, name: 'Log', path: 'logs', icon: 'heroInformationCircle' },
    { id: 4, name: 'Settings', path: 'settings', icon: 'heroCog6Tooth' },
    { id: 5, name: 'Notifications', path: 'notifications', icon: 'heroBell' },
  ];
}
