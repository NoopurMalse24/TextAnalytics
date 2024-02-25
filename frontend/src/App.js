// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import DataCleaningPage from './pages/DataCleaningPage';
import DataAnalysisPage from './pages/DataAnalysisPage'; // Import DataAnalysisPage component

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        <Route path="/data-cleaning" element={<DataCleaningPage />} />
        <Route path="/data-analysis" element={<DataAnalysisPage />} /> {/* Add route for DataAnalysisPage */}
      </Routes>
    </Router>
  );
}

export default App;
