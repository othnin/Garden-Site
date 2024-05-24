/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Function to initialize the chart
  function initChart(timeLabels, tempData, elementId) {
    var config = {
      type: 'line',
      data: {
        labels: timeLabels,
        datasets: [{
          data: tempData,
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#007bff',
          borderWidth: 4,
          pointBackgroundColor: '#007bff'
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        },
        legend: {
          display: false
        }
      }
    }

    // Graphs
    const ctx = document.getElementById(elementId).getContext('2d');
    // eslint-disable-next-line no-unused-vars
    const tempChart = new Chart(ctx, config);
  }

  // Expose the initChart function to the global scope
  window.initChart = initChart;

})();

