import { Injectable } from '@angular/core';
import { CanActivate, RouterStateSnapshot, ActivatedRouteSnapshot, Router } from '@angular/router';
import { SignupService } from './services/signup.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private signupService: SignupService, private router: Router) {}

  canActivate(
    route: ActivatedRouteSnapshot, 
    state: RouterStateSnapshot): boolean 
  {

    if (localStorage.getItem('seller')){
      return true
    }
    // Get the current value of isSellerLoggedIn
    const isLoggedIn = this.signupService.isSellerLoggedIn.getValue();
    
    // Return the boolean value
    return isLoggedIn; 
  } 
}
