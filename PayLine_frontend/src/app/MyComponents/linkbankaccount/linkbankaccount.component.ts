import { Component } from '@angular/core';

@Component({
  selector: 'app-linkbankaccount',
  templateUrl: './linkbankaccount.component.html',
  styleUrl: './linkbankaccount.component.css'
})
export class LinkbankaccountComponent {
  fullName: string = '';
  address: string = '';
  dob: Date | null = null;
  accountNumber: string = '';
  routingNumber: string = '';
  bankName: string = '';

  linkAccount() {
    // Perform logic to link bank account
    console.log('Linking bank account...');
    console.log('Full Name:', this.fullName);
    console.log('Address:', this.address);
    console.log('Date of Birth:', this.dob);
    console.log('Account Number:', this.accountNumber);
    console.log('Routing Number:', this.routingNumber);
    console.log('Bank Name:', this.bankName);
  }
}
