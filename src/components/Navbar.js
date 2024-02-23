// Navbar.js
import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Text Analytics</h1>
      <ul>
        <li><a href="/">Home</a></li>
        {/* Add more navigation links if needed */}
      </ul>
    </nav>
  );
}

export default Navbar;
