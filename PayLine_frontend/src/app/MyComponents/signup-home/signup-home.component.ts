import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router'; // Import ActivatedRoute and Router

@Component({
  selector: 'app-signup-home',
  templateUrl: './signup-home.component.html',
  styleUrls: ['./signup-home.component.css'] // Corrected styleUrls
})
export class SignupHomeComponent implements OnInit { // Implement OnInit interface

  name: any;

  constructor(public route: ActivatedRoute) { } // Corrected the constructor parameter name

  ngOnInit(): void {
    this.route.queryParams.subscribe((params: any) => { // Added parentheses around params
      console.log(params);
      this.name = params.data;
    });
  }
}
