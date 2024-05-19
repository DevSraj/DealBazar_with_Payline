import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  constructor (){}

  ngOnInit() {}

  Login(data:object): void{
    console.warn(data)


  }
}
