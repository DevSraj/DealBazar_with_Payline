import { Component } from '@angular/core';

@Component({
  selector: 'app-currency-conversion',
  templateUrl: './currency-conversion.component.html',
  styleUrls: ['./currency-conversion.component.css']
})
export class CurrencyConversionComponent {
  amount: number | null = null;
  fromCurrency: string = '';
  toCurrency: string = '';
  convertedAmount: number | null = null;

  // Sample conversion rates (for demonstration)
  conversionRates: { [key: string]: number } = {
    'USD': 1,  // 1 USD = 1 USD
    'EUR': 0.85,  // 1 USD = 0.85 EUR
    'GBP': 0.73,  // 1 USD = 0.73 GBP
    'JPY': 110.47,  // 1 USD = 110.47 JPY
    'CAD': 1.26  // 1 USD = 1.26 CAD
  };

  currencies: string[] = Object.keys(this.conversionRates); // Example currencies, you can extend this list

  convert() {
    // Check if amount, fromCurrency, and toCurrency are selected
    if (this.amount !== null && this.fromCurrency && this.toCurrency) {
      // Convert the amount
      const rateFrom = this.conversionRates[this.fromCurrency];
      const rateTo = this.conversionRates[this.toCurrency];
      this.convertedAmount = (this.amount * rateFrom) / rateTo;
    } else {
      // If any required field is missing, set convertedAmount to null
      this.convertedAmount = null;
    }
  }
}
