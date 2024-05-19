// profile.component.ts

import { Component, Input, OnInit } from '@angular/core';
import Chart from 'chart.js/auto'; // Import Chart.js

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  @Input() creditScore: number;

  // Sample profile data (replace with actual data)
  emailAddress: string = 'example@example.com';
  username: string = 'example_user';
  bank: string = 'Example Bank';
  address: string = '123 Example Street, City, Country';
  dob: string = '01/01/1990';
  bankName: string = 'Example Bank';

  constructor() { }

  ngOnInit(): void {
    this.renderExpenditureChart(); // Call the method to render the expenditure chart
  }

  renderExpenditureChart(): void {
    // Sample data (replace with actual data)
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const expenditureData = [100, 150, 200, 180, 220, 250, 300, 280, 320, 350, 400, 380]; // Sample expenditure data

    // Create a new chart instance
    new Chart('expenditureChart', {
      type: 'line',
      data: {
        labels: months,
        datasets: [{
          label: 'Expenditure',
          data: expenditureData,
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }
}
