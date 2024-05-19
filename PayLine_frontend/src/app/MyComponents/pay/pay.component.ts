import { Component } from '@angular/core';

@Component({
  selector: 'app-pay',
  templateUrl: './pay.component.html',
  styleUrls: ['./pay.component.css']
})
export class PayComponent {
  payTo: string = 'username';
  payVia: string = 'Username';
  recipient: string = '';
  amount: number;
  note: string = '';
  selectedCurrency: string = 'BTC'; // Default currency
  
  currencies = [
    { code: 'BTC', name: 'Bitcoin' },
    { code: 'ETH', name: 'Ethereum' },
    { code: 'XRP', name: 'Ripple' },
    { code: 'LTC', name: 'Litecoin' },
    { code: 'BCH', name: 'Bitcoin Cash' },
    { code: 'ADA', name: 'Cardano' },
    { code: 'DOT', name: 'Polkadot' },
    { code: 'LINK', name: 'Chainlink' },
    { code: 'XLM', name: 'Stellar' },
    { code: 'SOL', name: 'Solana' },
    // Add more currencies as needed
  ];

  constructor() { }

  updatePayVia() {
    switch (this.payTo) {
      case 'username':
        this.payVia = 'Username';
        break;
      case 'mobile':
        this.payVia = 'Mobile Number';
        break;
      case 'email':
        this.payVia = 'Email';
        break;
      default:
        this.payVia = 'Username';
    }
  }

  convertAmount() {
    // No need to perform conversion, just update the selected currency
  }

  pay() {
    console.log('Payment processing...');
    console.log('Pay via:', this.payTo);
    console.log('Recipient:', this.recipient);
    console.log('Amount:', this.amount);
    console.log('Note:', this.note);
    console.log('Selected Currency:', this.selectedCurrency);
  }
}
