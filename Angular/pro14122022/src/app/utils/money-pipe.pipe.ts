import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'moneyPipe' })
export class moneyPipe implements PipeTransform {
  transform(value: number, currency: string): string {
    return value + currency.toUpperCase();
  }
}