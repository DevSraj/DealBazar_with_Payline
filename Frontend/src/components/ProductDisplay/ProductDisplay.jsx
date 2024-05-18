import React ,{ useContext, useState } from 'react'
import './ProductDisplay.css'
import star_icon from '../assets/star_icon.png'
import star_dull_icon from '../assets/star_dull_icon.png'
import { ShopContext } from '../../context/ShopContext'
const ProductDisplay = (props) => {
    const {product}=props;

    const {addToCart} = useContext(ShopContext);
    const [selectedSize, setSelectedSize] = useState(null);
    const [showPopup, setShowPopup] = useState(false);
    const [selectedProduct, setSelectedProduct] = useState(null);
    const handleClick = (size) => {
        setSelectedSize(size);
      };

      const handleAddToCart = (productId) => {
        addToCart(productId);
        setSelectedProduct(productId);
        setShowPopup(true);
    };

    const handleContinueShopping = () => {
        setShowPopup(false);
    };
    
  return (
    <div className='productdisplay'>
        <div className="productdisplay-left">
            <div className="productdisplay-img-list">
               <img src={product.image} alt=''/> 
               <img src={product.image} alt=''/> 
               <img src={product.image} alt=''/> 
               <img src={product.image} alt=''/> 
            </div>
                <div className="productdisplay-img">
                    <img className="productdisplay-main-img"src={product.image} alt=''/>
                </div>
        </div>
        <div className="productdisplay-right">
            <h1>{product.name}</h1>
            <div className="productdisplay-right-star">
                <img src={star_icon} alt=''/>
                <img src={star_icon} alt=''/>
                <img src={star_icon} alt=''/>
                <img src={star_icon} alt=''/>
                <img src={star_dull_icon} alt=''/>
                <p>( 122  )</p>
            </div>
            <div className='productdisplay-right-prices'>
                <div className="productdisplay-right-price-old">
                    ${product.old_price}
                </div>
                <div className="productdisplay-right-price-new">
                    ${product.new_price}
                </div>
            </div>
            <div className="productdisplay-right-description">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Expedita, eligendi harum in quas quasi distinctio ducimus quaerat, earum reiciendis minus porro nulla, voluptatibus labore suscipit ut hic dolore similique quidem.
            </div>
            <div className="productdisplay-right-size">
                <h1>Select size</h1>
                <h1/>
                <div className="productdisplay-right-size-select">
                <div className={selectedSize === 'S' ? 'selected' : ''} onClick={() => handleClick('S')}>S</div>
                <div className={selectedSize === 'M' ? 'selected' : ''} onClick={() => handleClick('M')}>M</div>
                <div className={selectedSize === 'L' ? 'selected' : ''} onClick={() => handleClick('L')}>L</div>
                <div className={selectedSize === 'XL' ? 'selected' : ''} onClick={() => handleClick('XL')}>XL</div>
                <div className={selectedSize === 'XXL' ? 'selected' : ''} onClick={() => handleClick('XXL')}>XXL</div>

                    {/* Add more size divs as needed */}
                </div>
            </div>
            <button onClick={()=> handleAddToCart(product.id)}>ADD TO CART</button>
            {/* Popup */}
            {showPopup && (
                <div className="popup">
                    <div className="popup-content">
                        <span className="close" onClick={() => setShowPopup(false)}>&times;</span>
                        <p>Item successfully added to cart !</p>
                        <button className="pop-button"onClick={handleContinueShopping}>Continue Shopping</button>
                    </div>
                </div>
            )}
            <p className="productdisplay-right-category"><span>Category :</span>Women, T-Shirt ,Crop Top</p>
            <p className="productdisplay-right-category"><span>Tags:</span>Modern, Latest </p>

        </div>

    </div>
  )
}

export default ProductDisplay