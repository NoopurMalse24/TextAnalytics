// DataCleaningPage.js
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './DataCleaningPage.css'; // Import CSS file for styling

const DataCleaningPage = () => {
  const navigate = useNavigate();

  // Use useEffect to navigate to DataAnalysisPage after 5 seconds
  useEffect(() => {
    const timeout = setTimeout(() => {
      navigate('/data-analysis');
    }, 5000);

    return () => clearTimeout(timeout); // Clear the timeout if component unmounts
  }, [navigate]);

  return (
    <div className="data-cleaning-page">
      <div className="loading-container">
        <div className="spinner">
          <div className="bounce1"></div>
          <div className="bounce2"></div>
          <div className="bounce3"></div>
        </div>
        <p>Your data is being cleaned. Please wait...</p>
      </div>
    </div>
  );
}

export default DataCleaningPage;
