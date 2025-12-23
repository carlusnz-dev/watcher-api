import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Monitor {
  private baseURL = 'http://127.0.0.1:5000/api/monitor';
  constructor(private http: HttpClient) {}

  // Get All Monitors
  getAllMonitors(): Observable<any> {
    return this.http.get(`${this.baseURL}/read_all`);
  }
}
