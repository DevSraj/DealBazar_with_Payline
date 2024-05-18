import React from 'react'
import './CSS/LoginSignup.css'
const LoginSignup = () => {
  return (
    <div className='loginsigup'>
      <div className="loginsignup-container">
        <h1>Sign up</h1>
        <div className="loginsignup-field">
          <input type="text" placeholder='Your name '/>
          <input type="email" placeholder='Email Address'/>
          <input type="password" placeholder='Password'/>
        </div>
        <button>Continue</button>
        <p className="loginsignup-login">Already have an account? <span>Login</span></p>
        <div className="loginsignup-agree">
          <input type="checkbox" name='' id =''/>
          <p>By continuing , i agree to the terms of use & provacy policy</p>
        </div>
      </div>

    </div>
  )
}

export default LoginSignup