import { Component, computed, inject, resource } from '@angular/core';
import { MonitorService } from '../../../services/monitor-service';
import { Router } from '@angular/router';
import { ButtonComponent } from '../../button-component/button-component';

@Component({
  selector: 'app-home-component',
  imports: [ButtonComponent],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})
export class HomeComponent {
  private monitorService = inject(MonitorService);
  private router = inject(Router);
  private monitors = this.monitorService.getAllMonitors();

  // handlers
  handleNavigation(path: string) {
    this.router.navigate([path]);
  }

  dataMonitor = resource({
    loader: () => this.monitors,
  });

  activeMonitor = computed(() => {
    const all = this.dataMonitor.value();
    if (!all) return [];
    return all.filter((m) => m.status === 200);
  });

  deactivedMonitors = computed(() => {
    const all = this.dataMonitor.value();
    if (!all) return [];
    return all.filter((m) => m.status !== 200);
  });

  totalCount = computed(() => this.dataMonitor.value()?.length ?? 0);
}
