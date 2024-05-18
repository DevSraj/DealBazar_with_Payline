import React from 'react'
import './Hero.css'
import hand_icon from '../assets/hand_icon.png'
import arrow_icon from '../assets/arrow.png'
import hero_image from '../assets/hero_image.png'
import { Link } from 'react-router-dom';


const Hero = () => {
   
  return (
    <div className='hero'>
        <div className="hero-left">
            <h2>New Arrivals Only</h2>
            <div className="hand-hand-icon">
                 <p>New</p>
                <img src={hand_icon} alt="handit" />
            </div>
            <div className='left-para'>
            <p>Collection</p>
            <p>For Everyone</p>
            </div>
            
        <div className="hero-latest-btn">
            <div>
            <Link to="/new-collections" style={{ textDecoration: 'none', color: 'white',transition: 'color 0.3s ease' }}>

                Latest Collection
                </Link>
                </div>
                <img src={arrow_icon} alt="arrow" />
            </div>
            
        </div>

        <div className="hero-right">
            <img src={hero_image} alt="hero_image"/>

        </div>
        
    </div>
    
  )
}

export default Hero