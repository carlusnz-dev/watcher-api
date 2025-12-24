import { NgClass } from '@angular/common';
import { Component, input, output } from '@angular/core';

@Component({
  selector: 'app-button-component',
  standalone: true,
  template: `
    <button
      class="px-4 py-2 rounded-2xl font-bold hover:px-7 transition-all cursor-pointer"
      [ngClass]="{
        'bg-linear-to-r from-blue-500 to-indigo-600 text-white': variant() === 'primary',
        'bg-transparent inset-ring-4 inset-ring-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white':
          variant() === 'secondary'
      }"
      (click)="onAction.emit()"
    >
      {{ label() }}
    </button>
  `,
  imports: [NgClass],
})
export class ButtonComponent {
  label = input.required<string>();
  variant = input<string>('primary');
  onAction = output();
}
