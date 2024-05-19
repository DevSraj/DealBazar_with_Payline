import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms'; // Import NgForm for form handling
import { SignupService } from '../../services/signup.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  constructor(private signup: SignupService, private router: Router) { }
  showLogin = false;
  name: any;

  ngOnInit() {
  }

  signUp(formData: any): void {
    const { email, name, password } = formData; // Changed from username to name
    const signUpData = { email, name: name || '', password }; // Use name or provide a default value if null
    this.signup.userSignUp(signUpData).subscribe((result) => {
      if (result) {
        this.signup.setUsername(name || ''); // Use name or provide a default value if null
        this.router.navigate(['signup-home']);
      }
    });
  }

  navToSecondComp() {
    this.router.navigate(['/signup-home'], { queryParams: { data: this.name } });
  }
}
