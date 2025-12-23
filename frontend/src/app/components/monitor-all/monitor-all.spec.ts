import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MonitorAll } from './monitor-all';

describe('MonitorAll', () => {
  let component: MonitorAll;
  let fixture: ComponentFixture<MonitorAll>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MonitorAll]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MonitorAll);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
