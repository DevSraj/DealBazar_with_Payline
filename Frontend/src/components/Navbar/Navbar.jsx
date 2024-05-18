import React, { useContext, useState } from 'react';
import './Navbar.css'; 
import logo from '../assets/logo.png'
import cart_icon from '../assets/cart_icon.png'
import { Link } from 'react-router-dom';
import { ShopContext } from '../../context/ShopContext';

const Navbar = () => {
  const [activeTab, setActiveTab] = useState(null);
  const {getTotalCartItems}=useContext(ShopContext);

  const handleClick = (index) => {
    setActiveTab(index);
  };


  return (
    <div className="navbar">
      <div className="nav-logo">
        <img src={logo} alt="logo" />
        <p>SHOPPER</p>
      </div>
      <ul className="nav-menu">
        <li className={activeTab === 0 ? 'active' : ''} onClick={() => handleClick(0)}><Link style={{textDecoration:'none',color:'#f00000'}}to='/'>Shop</Link></li>
        <li className={activeTab === 1 ? 'active' : ''} onClick={() => handleClick(1)}><Link style={{textDecoration:'none',color:'#f00000'}}to='/mens'>Men</Link></li>
        <li className={activeTab === 2 ? 'active' : ''} onClick={() => handleClick(2)}><Link style={{textDecoration:'none',color:'#f00000'}}to='/womens'>Women</Link></li>
        <li className={activeTab === 3 ? 'active' : ''} onClick={() => handleClick(3)}><Link style={{textDecoration:'none',color:'#f00000'}}to='/kids'>Kids</Link></li>
      </ul>

      <div className="nav-login-cart" >
        <Link to='/login'><button>Login</button></Link>
        <Link to='/cart'><img src={cart_icon} alt="cart"/> </Link>
        <div className="nav-cart-count">{getTotalCartItems()}</div>
      </div>
    </div>
  );
};

export default Navbar;
