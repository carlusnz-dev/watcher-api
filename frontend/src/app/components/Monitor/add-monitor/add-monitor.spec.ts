import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddMonitor } from './add-monitor';

describe('AddMonitor', () => {
  let component: AddMonitor;
  let fixture: ComponentFixture<AddMonitor>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddMonitor]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddMonitor);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
