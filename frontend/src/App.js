// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import DataCleaningPage from './pages/DataCleaningPage';
import DataAnalysisPage from './pages/DataAnalysisPage';
import OverallAnalysisPage from './pages/OverallAnalysisPage';
import SkewedPage from './pages/SkewedPage';
import VBCPage from './pages/VBCPage'; // Import VBCPage component

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        <Route path="/data-cleaning" element={<DataCleaningPage />} />
        <Route path="/data-analysis" element={<DataAnalysisPage />}/>
        <Route path="/overall-analysis" element={<OverallAnalysisPage />} />
        <Route path="/skewed-page" element={<SkewedPage />} />
        <Route path="/VBC" element={<VBCPage />} />
      </Routes>
    </Router>
  );
}

export default App;
