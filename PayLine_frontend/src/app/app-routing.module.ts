import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './MyComponents/login/login.component';
import { SignupComponent } from './MyComponents/signup/signup.component';
import { SignupHomeComponent } from './MyComponents/signup-home/signup-home.component';
import { FrontPageComponent } from './MyComponents/front-page/front-page.component'; // Import the FrontPageComponent
import { AuthGuard } from './auth.guard';
import { CurrencyConversionComponent } from './MyComponents/currency-conversion/currency-conversion.component';
import { HeaderComponent } from './MyComponents/header/header.component';
import { PayComponent } from './MyComponents/pay/pay.component';
import { LinkbankaccountComponent } from './MyComponents/linkbankaccount/linkbankaccount.component';
import { ProfileComponent } from './MyComponents/profile/profile.component';
import { InstantLoanComponent } from './MyComponents/instantloan/instantloan.component';

const routes: Routes = [
 // Route to FrontPageComponent by default
 { path: '', component: FrontPageComponent },
 { path: '', component: HeaderComponent },
 { path: 'instantloan', component: InstantLoanComponent},
 {path:'pay',component : PayComponent},
 {path:'linkbankaccount',component : LinkbankaccountComponent},
 {path:'profile',component :ProfileComponent},
  { path: 'currency-conversion', component: CurrencyConversionComponent },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'signup-home', component: SignupHomeComponent },
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
