import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';

export interface Monitor {
  id: number;
  name: string;
  status: number;
  frequency: number;
  description: string;
  url: string;
}

@Injectable({
  providedIn: 'root',
})
export class MonitorService {
  private http = inject(HttpClient);
  private baseUrl = 'http://127.0.0.1:5000/api/monitor';

  async getAllMonitors(): Promise<Monitor[]> {
    const response = await firstValueFrom(this.http.get<any>(this.baseUrl + '/read_all'));
    const monitors = response.monitors;
    return monitors;
  }
}
