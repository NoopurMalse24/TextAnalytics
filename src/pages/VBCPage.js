import React, { useState, useEffect, useRef } from 'react';
import './VBCPage.css';
import Chart from 'chart.js/auto';
import Navbar from '../components/Navbar';

const VBCPage = () => {
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedSubcategory, setSelectedSubcategory] = useState('');
  const [products, setProducts] = useState([]);

  const productListRef = useRef(null);
  const chartRef = useRef(null);
  const chartInstanceRef = useRef(null);

  const categories = [
    { name: 'Category 1', subcategories: ['Subcategory 1.1', 'Subcategory 1.2', 'Subcategory 1.3'] },
    { name: 'Category 2', subcategories: ['Subcategory 2.1', 'Subcategory 2.2', 'Subcategory 2.3'] },
  ];

  const handleCategoryChange = (event) => {
    const category = event.target.value;
    setSelectedCategory(category);
    setSelectedSubcategory('');
  };

  const handleSubcategoryChange = (event) => {
    const subcategory = event.target.value;
    setSelectedSubcategory(subcategory);
  };

  const fetchProducts = () => {
    const filteredProducts = [
      { id: 1, name: 'Product 1', description: 'Description for Product 1', imageUrl: 'https://via.placeholder.com/150' },
      { id: 2, name: 'Product 2', description: 'Description for Product 2', imageUrl: 'https://via.placeholder.com/150' },
      { id: 3, name: 'Product 3', description: 'Description for Product 3', imageUrl: 'https://via.placeholder.com/150' },
      { id: 4, name: 'Product 4', description: 'Description for Product 4', imageUrl: 'https://via.placeholder.com/150' },
      { id: 5, name: 'Product 5', description: 'Description for Product 5', imageUrl: 'https://via.placeholder.com/150' },
      { id: 6, name: 'Product 6', description: 'Description for Product 6', imageUrl: 'https://via.placeholder.com/150' },
    ];
    setProducts(filteredProducts);
  };

  useEffect(() => {
    if (selectedCategory && selectedSubcategory) {
      fetchProducts();
    }
  }, [selectedCategory, selectedSubcategory]);

  useEffect(() => {
    if (products.length > 0 && chartRef.current) {
      if (chartInstanceRef.current) {
        chartInstanceRef.current.destroy();
      }
      const ctx = chartRef.current.getContext('2d');
      chartInstanceRef.current = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
          datasets: [{
            label: 'Demo Chart',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
  }, [products]);

  return (
    <div>
      <Navbar />
    <div className="vbc-container">
      <h2>View by Category</h2>
      <div className="select-container">
        <label htmlFor="category">Select Category:</label>
        <select id="category" value={selectedCategory} onChange={handleCategoryChange}>
          <option value="">Select...</option>
          {categories.map((category, index) => (
            <option key={index} value={category.name}>{category.name}</option>
          ))}
        </select>
      </div>
      <div className="select-container">
        <label htmlFor="subcategory">Select Subcategory:</label>
        <select id="subcategory" value={selectedSubcategory} onChange={handleSubcategoryChange} disabled={!selectedCategory}>
          <option value="">Select...</option>
          {selectedCategory &&
            categories.find(cat => cat.name === selectedCategory).subcategories.map((subcategory, index) => (
              <option key={index} value={subcategory}>{subcategory}</option>
            ))
          }
        </select>
      </div>
      <h3>Products:</h3>
      <div className="product-list-container">
        <div ref={productListRef} className="product-list">
          {products.map(product => (
            <div key={product.id} className="product-item">
              <img src={product.imageUrl} alt={`Product ${product.id}`} />
              <div className="product-details">
                <p className="product-name">{product.name}</p>
                <p className="product-description">{product.description}</p>
                <p className="product-id">ID: {product.id}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="chart-container">
        <canvas ref={chartRef}></canvas>
      </div>
    </div>
    </div>
  );
};

export default VBCPage;
