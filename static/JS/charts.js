anychart.onDocumentReady(function() {

    // set the data
    var data = [
        {x: "Total Population", value: 823126},
        {x: "Homeless", value: 6718}
    ];
  
    // create the chart
    var chart = anychart.pie();
  
    // set the chart title
    chart.title("Total population vs homeless people 2019");
  
    // add the data
    chart.data(data);
  
    // display the chart in the container
    chart.container('container');
    chart.draw();
  
  });