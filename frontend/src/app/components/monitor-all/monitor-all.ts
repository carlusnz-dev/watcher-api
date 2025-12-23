import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { Monitor } from '../../services/monitor';

@Component({
  selector: 'app-monitor-all',
  imports: [],
  templateUrl: './monitor-all.html',
  styleUrl: './monitor-all.css',
})
export class MonitorAll implements OnInit {
  constructor(private monitorService: Monitor, private cdr: ChangeDetectorRef) {}
  monitors: any[] = [];

  ngOnInit(): void {
    this.monitorService.getAllMonitors().subscribe((data) => {
      const list = data['monitors'];
      this.monitors = list;

      console.log('Lista salva:', this.monitors);
      this.cdr.detectChanges();
    });
  }
}
