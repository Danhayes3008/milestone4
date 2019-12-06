anychart.onDocumentReady(function() {
 
    // set the data
    var data = {
        header: ["Name", "Death toll"],
        rows: [
          ["1995", 3951],
          ["2000", 4587],
          ["2005", 5174],
          ["2010", 5922],
          ["2015", 6718]
    ]};

    // create the chart
    var chart = anychart.column();

    // add the data
    chart.data(data);

    // set the chart title
    chart.title("The deadliest earthquakes in the XXth century");

    // draw
    chart.container("bar");
    chart.draw();
  });