import React, { useEffect } from 'react';
import Chart from 'chart.js/auto'; // Import Chart.js
import Navbar from '../components/Navbar';
import './DataAnalysisPage.css'; // Import CSS for styling

const DataAnalysisPage = () => {
  useEffect(() => {
    // Generate random data for demonstration
    const labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'];
    const data = [Math.random() * 100, Math.random() * 100, Math.random() * 100, Math.random() * 100, Math.random() * 100];

    // Draw bar chart for each analysis block with animation
    drawBarChart('Descriptive', labels, data, true);
    drawBarChart('Sentiment', labels, data, true);
    drawBarChart('KeyPhrase', labels, data, true);
    drawBarChart('Rating', labels, data, true);
    drawBarChart('TopicModelling', labels, data, true);
    drawBarChart('Summarization', labels, data, true);
  }, []); // Run only once on component mount

  // Function to draw bar chart
  const drawBarChart = (analysisType, labels, data, animate) => {
    const ctx = document.getElementById(`barChart-${analysisType}`).getContext('2d');

    // Destroy existing chart instance if it exists
    if (window.barChartInstances && window.barChartInstances[analysisType]) {
      window.barChartInstances[analysisType].destroy();
    }

    // Create new chart instance
    window.barChartInstances = window.barChartInstances || {};
    window.barChartInstances[analysisType] = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: `${analysisType} Bar Chart`,
          data: data,
          backgroundColor: 'rgba(54, 162, 235, 0.5)', // Blue color
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        animation: {
          duration: animate ? 1000 : 0 // Add animation if enabled
        }
      }
    });
  };

  // Function to handle PDF download
  const handleDownloadPDF = () => {
    // Implement PDF download logic here
    alert('PDF Downloaded Successfully');
  };

  return (
    <div className="data-analysis-page">
      <Navbar />
      <div className="container">
        <h2>Data Analysis</h2>
        <div className="analysis-block">
          <h3>Descriptive Analysis</h3>
          <canvas id="barChart-Descriptive" width="400" height="100"></canvas>
        </div>

        <div className="analysis-block">
          <h3>Sentiment Analysis</h3>
          <canvas id="barChart-Sentiment" width="400" height="100"></canvas>
        </div>

        <div className="analysis-block">
          <h3>Key Phrase Extraction</h3>
          <canvas id="barChart-KeyPhrase" width="400" height="100"></canvas>
        </div>

        <div className="analysis-block">
          <h3>Rating Analysis</h3>
          <canvas id="barChart-Rating" width="400" height="100"></canvas>
        </div>

        <div className="analysis-block">
          <h3>Topic Modelling</h3>
          <canvas id="barChart-TopicModelling" width="400" height="100"></canvas>
        </div>

        <div className="analysis-block">
          <h3>Summarization</h3>
          <canvas id="barChart-Summarization" width="400" height="100"></canvas>
        </div>
        
        <button className="download-pdf-button" onClick={handleDownloadPDF}>Download PDF</button>
      </div>
    </div>
  );
}

export default DataAnalysisPage;
