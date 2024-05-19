// instant-loan.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-instant-loan',
  templateUrl: './instantloan.component.html',
  styleUrls: ['./instantloan.component.css']
})
export class InstantLoanComponent {
  selectedCurrency: string = 'BTC'; // Default currency selection
  amount: number = 0; // Initial loan amount

  currencies: { code: string, name: string }[] = [
    { code: 'BTC', name: 'Bitcoin' },
    { code: 'ETH', name: 'Ethereum' },
    { code: 'LTC', name: 'Litecoin' },
    { code: 'XRP', name: 'Ripple (XRP)' },
    // Add more currencies here
  ];

  constructor() { }

  // Handle loan calculation or other logic here
  getInstantLoan() {
    // Your logic to process the loan request
    console.log(`Requesting instant loan in ${this.selectedCurrency} for amount ${this.amount}`);
    // Implement your loan processing logic here
  }
}
