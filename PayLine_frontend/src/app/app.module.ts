import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './MyComponents/header/header.component';
import { LoginComponent } from './MyComponents/login/login.component';
import { SignupComponent } from './MyComponents/signup/signup.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { SignupHomeComponent } from './MyComponents/signup-home/signup-home.component';
import { FrontPageComponent } from './MyComponents/front-page/front-page.component';
import { CurrencyConversionComponent } from './MyComponents/currency-conversion/currency-conversion.component';
import { PayComponent } from './MyComponents/pay/pay.component';
import { LinkbankaccountComponent } from './MyComponents/linkbankaccount/linkbankaccount.component';
import { ProfileComponent } from './MyComponents/profile/profile.component';
import { InstantLoanComponent } from './MyComponents/instantloan/instantloan.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    SignupComponent,
    SignupHomeComponent,
    FrontPageComponent,
    CurrencyConversionComponent,
    PayComponent,
    LinkbankaccountComponent,
    ProfileComponent,
    InstantLoanComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
