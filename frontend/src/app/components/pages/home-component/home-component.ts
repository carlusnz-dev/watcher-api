import { Component, inject, resource } from '@angular/core';
import { MonitorService } from '../../../services/monitor-service';

@Component({
  selector: 'app-home-component',
  imports: [],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})
export class HomeComponent {
  private monitorService = inject(MonitorService);

  dataMonitor = resource({
    loader: () => this.monitorService.getAllMonitors(),
  });
}
