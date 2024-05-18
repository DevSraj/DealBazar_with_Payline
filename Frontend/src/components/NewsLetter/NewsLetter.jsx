import React from 'react'
import './NewsLetter.css'

const NewsLetter = () => {
  return (
    <div className='newsletter'>
        <h1>Get Exclusive Offers On Your Email</h1>
        <p>Subscribe to our Newslettes and stay Updated</p>

        <div>
            <input type='email' placeholder='Your Email id'></input>
            <button>Subscribe</button>
        </div>
    </div>
  )
}

export default NewsLetter