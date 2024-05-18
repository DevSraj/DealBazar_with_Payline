import React,{useContext} from 'react'
import './CartItem.css'
import { ShopContext } from '../../context/ShopContext'
import remove_icon from '../assets/cart_cross_icon.png'
const CartItems = () => {
    const {getTotalCartAmount,all_product,cartItems,removeFromCart}=useContext(ShopContext);

  return (
    <div className="cartitems">
        <div className="cartitems-format-main">
        <p>Product</p>
        <p>Title</p>
        <p>Price</p>
        <p>Quantity</p>
        <p>Total</p>
        <p>Remove</p>
    </div>
    <hr/>
    {all_product.map((e)=>{
        if(cartItems[e.id]>0){
            return<div>
            <div className="cartitems-format cartitems-format-main">
                <img src={e.image} alt="" className='cartitems-product-icon'/>
                <p>{e.name}</p>
                
                <p>${e.new_price}</p>
                <p className='cartitems-quantity'>{cartItems[e.id]}</p>
                    <p>$ {e.new_price*cartItems[e.id]}</p>
                    <img className="cartitems-remove-icon"src={remove_icon} alt='' onClick={()=>{removeFromCart(e.id)}}/>  
            </div>
            <hr/>
            </div>
        }
        return null;
    })}
    <div className="cartitems-down">
        <div className="cartitems-total">
            <h1>Cart Total</h1>
            <div className="cartitems-total-items">
                <p>Subtotal</p>
                <p>${getTotalCartAmount()}</p>
            </div>
            <hr/>
            <div className="cartitems-total-items">
                <p>Shipping fee</p>
                <p>Free</p>
            </div>
            <hr/>
            <div className="cartitems-total-items">
                <h3>Total</h3>
                <h3>${getTotalCartAmount()}</h3>
            </div>
            <button>PROCEED TO CHECKOUT</button>
        </div>
        <div className="cartitems-promocode">
        <p> If You Have a promo code, Enter It Here</p>
        <div className="cartitems-promobox">
            <input type="text" placeholder='Enter Promo Code'/>
            <button>Apply</button>
        </div>

    </div>
    </div>
    
    </div>

  )
}

export default CartItems