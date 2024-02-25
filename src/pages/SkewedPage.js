import React, { useState } from 'react';
import './SkewedPage.css';
import Navbar from '../components/Navbar';

const SkewedPage = () => {
  // State to store the product ID and product details
  const [productId, setProductId] = useState('');
  const [productDetails, setProductDetails] = useState(null);

  // Function to handle input change
  const handleInputChange = (event) => {
    setProductId(event.target.value);
  };

  // Function to handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Here, you would typically fetch product details from the backend using productId
      // For demo purposes, let's assume we have some sample data for demo products
      const demoProductData = {
        id: productId,
        name: `Demo Product ${productId}`,
        imageUrl: `https://via.placeholder.com/150?text=Product+${productId}`,
        // Add more properties as needed
      };
      // Update productDetails state with demo product data
      setProductDetails(demoProductData);
      // Clear the productId state after form submission
      setProductId('');
    } catch (error) {
      console.error('Error fetching product details:', error.message);
    }
  };

  return (
    <div>
      <Navbar />
    <div className="skewed-page-container">
      <h2>Search by Product ID</h2>
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <label htmlFor="productId">Product ID:</label>
          <input
            type="text"
            id="productId"
            value={productId}
            onChange={handleInputChange}
            placeholder="Enter Product ID"
            required
          />
          <button type="submit">Submit</button>
        </form>
      </div>
      {/* Display product details and graphs if available */}
      {productDetails && (
        <div className="product-details">
          <h3>Product Details</h3>
          <p>Name: {productDetails.name}</p>
          <img src={productDetails.imageUrl} alt={`Product ${productId}`} />
          {/* Display graphs related to the product */}
          {/* Add your chart components here */}
        </div>
      )}
    </div>
    </div>
  );
};

export default SkewedPage;
