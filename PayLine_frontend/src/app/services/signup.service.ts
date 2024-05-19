import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs'; // Retained imports
import { SignUp } from '../datatype'; // Retained import

@Injectable({
  providedIn: 'root'
})
export class SignupService {
  isSellerLoggedIn = new BehaviorSubject<boolean>(false);
  private username: string; // New property to store the username

  constructor(private http :HttpClient) { }

  userSignUp(data: SignUp): Observable<any> {
    return this.http.post('http://localhost:3000/signup', data);
  }

  // New method to set the username
  setUsername(username: string): void {
    this.username = username;
  }

  // New method to get the username
  getUsername(): string {
    return this.username;
  }
}
