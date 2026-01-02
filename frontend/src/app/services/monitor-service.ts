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

  async createNewMonitor(data: any): Promise<any> {
    const response = await firstValueFrom(this.http.post<any>(this.baseUrl + '/add', data));
    return response;
  }

  async updateMonitor(id: number, data: any): Promise<any> {
    const response = await firstValueFrom(this.http.put<any>(this.baseUrl + `/update/${id}`, data));
    return response;
  }

  async deleteMonitor(id: number): Promise<any> {
    const response = await firstValueFrom(this.http.delete<any>(this.baseUrl + `/delete/${id}`));
    return response;
  }
}
