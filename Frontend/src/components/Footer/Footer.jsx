import React from 'react'
import './Footer.css'
import footer_logo from '../assets/logo_big.png'
import instagram_icon from '../assets/instagram_icon.png'
import pintester_icon from '../assets/pintester_icon.png'
import whatsapp_icon from '../assets/whatsapp_icon.png'


const Footer = () => {
  return (
    <div className='footer'>
        <div className="footer-logo">
            <img src={footer_logo} alt=""/>
            <p className="brand">Shopper</p>
            <ul className="footer-links">
            <li>
                <a href="#">Company</a>
            </li>
            <li>
                <a href="#">Products</a>
            </li>
            <li>
                <a href="#">Policies</a>
            </li>
            <li>
                <a href="#">About</a>
            </li>
            <li>
                <a href="#">Contact</a>
            </li>

        </ul>
        </div>
        <div className="footer-description">
        <h2>Shopper is an online shopping platform .</h2>
        <p>
            
        Shopper is an online shopping platform that provides a wide range of products to its customers.</p>
        </div>
        
        <div className="footer-social-icon">
    <div>
        <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer">
            <img src={instagram_icon} alt="Instagram" />
        </a>
    </div>
    <div>
        <a href="https://www.pinterest.com" target="_blank" rel="noopener noreferrer">
            <img src={pintester_icon} alt="Pinterest" />
        </a>
    </div>
    <div>
        <a href="https://www.whatsapp.com" target="_blank" rel="noopener noreferrer">
            <img src={whatsapp_icon} alt="Whatsapp" />
        </a>
    </div>
</div>

        <div className="footer-copyright">
            <hr/>
            <p>Copyright © 2024 Shopper. All rights reserved.</p>
        </div>
    </div>
  )
}

export default Footer