// LandingPage.js
import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import ImageGallery from './ImageGallery'; // Import the ImageGallery component

const LandingPage = () => {
  const navigate = useNavigate();
  const [fileError, setFileError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const fileInput = e.target.querySelector('input[type="file"]');
    const file = fileInput.files[0];

    // Check if a file is selected
    if (!file) {
      setFileError('Please select a file');
      return;
    }

    // Check if the selected file is a .csv file
    if (file.type !== 'text/csv') {
      setFileError('Please select a .csv file');
      return;
    }

    // Proceed to the next page if file is valid
    navigate('/data-cleaning');
  };

  return (
    <div>
      <Navbar />
      <div className="container">
        <h2>InsightPlus: Customer Feedback Analytics Suite</h2>
        <ImageGallery />
        <p className="text-analysis">
          Text analysis is a crucial aspect of understanding large volumes of textual data. It involves various techniques such as sentiment analysis, key phrase extraction, topic modeling, and more, to derive meaningful insights from text. At our Text Analytics platform, we utilize advanced algorithms and visualizations to make text analysis both efficient and insightful.
        </p>
        <form onSubmit={handleSubmit}>
          <input type="file" accept=".csv" />
          {fileError && <div className="error">{fileError}</div>}
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
};

export default LandingPage;
