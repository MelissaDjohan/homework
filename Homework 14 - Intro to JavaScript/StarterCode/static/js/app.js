// from data.js
var tableData = data;
console.log(tableData);

// begin table 
// reference to the table body
var tbody = d3.select("tbody");

// console.log the data from data.js
console.log(data);

// // step 1: loop through data and console.log each report object
// data.forEach(function(sightingReport) {
//     console.log(sightingReport);
// });

// // step 2: use d3 to append one table row `tr` for each weather report object
// data.forEach(function(sightingReport) {
//     console.log(sightingReport);
//     var row = tbody.append("tr");
// });

// // step 3: use `Object.entries` to console.log each report value 
// data.forEach(function(sightingReport) {
//     console.log(sightingReport);
//     var row = tbody.append("tr");

//     Object.entries(sightingReport).forEach(function([key, value]) {
//         console.log(key, value);
//     });
// });

// // step 4: use d3 to append 1 cell per report value (datetime, city, state, country, shape, durationMinutes, comments)
// data.forEach(function(sightingReport) {
//     console.log(sightingReport);
//     var row = tbody.append("tr");

//     Object.entries(sightingReport).forEach(function([key, value]) {
//         console.log(key, value);
//         // append a cell to the row for each value
//         var cell = row.append("td");
//     });
// });

// // step 5: use d3 to upsate each cell's text with report values (datetime, city, state, country, shape, durationMinutes, comments)
// data.forEach(function(sightingReport) {
//     console.log(sightingReport);
//     var row = tbody.append("tr");

//     Object.entries(sightingReport).forEach(function([key, value]) {
//         console.log(key, value);
//         // append a cell to the row for each value
//         var cell = row.append("td");
//         cell.text(value);
//     });
// });

// to do with arrow functions:
data.forEach((sightingReport) => {
    var row = tbody.append("tr");
    Object.entries(sightingReport).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
    });
});

// button and filters:

var button = d3.select("#filter-btn");

// filter for date (you will have to data.pass because the data is a string)
button.on("click", function() {
    d3.event.preventDefault();
    var dateInput = d3.select("#datetime");
    var dateInputValue = dateInput.property("value");
    console.log(dateInputValue);
    console.log(tableData);
    var filteredData = tableData.filter(tableData => tableData.datetime === dateInput);
    buildTable(filteredData);
});

function buildTable(filteredDateTable) {
    filteredData.forEach((dateData) => {
        var row = tbody.append("tr");
        Object.entries(dateData).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
});


// filter for city
button.on("click", function() {
    var cityInput = d3.select("#city");
    var cityInputValue =cityInput.property("value");
    console.log(cityInputValue);
    console.log(tableData);
    var filteredData1 = tableData.filter(tableData => tableData.city === cityInput);
    buildTable(filteredData1);
});

function buildTable(filteredCityTable) {
    filteredData1.forEach((cityData) => {
        var row = tbody.append("tr");
        Object.entries(cityData).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });
};

// filter for state
button.on("click", function() {
    var stateInput = d3.select("#state");
    var stateInputValue =stateInput.property("value");
    console.log(stateInputValue);
    console.log(tableData);
    var filteredData2 = tableData.filter(tableData => tableData.state === stateInput);
    buildTable(filteredData2);
});

function buildTable(filteredStateTable) {
    filteredData2.forEach((stateData) => {
        var row = tbody.append("tr");
        Object.entries(stateData).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });
};

// filter for country
button.on("click", function() {
    var countryInput = d3.select("#country");
    var countInputValue = countryInput.property("value");
    console.log(countInputValue);
    console.log(tableData);
    var filteredData3 = tableData.filter(tableData => tableData.country === countryInput);
    buildTable(filteredData3);
});

function buildTable(filteredCountryTable) {
    filteredData3.forEach((countryData) => {
        var row = tbody.append("tr");
        Object.entries(countryData).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });
};

// filter for shape
button.on("click", function() {
    var shapeInput = d3.select("#shape");
    var shapeInputValue = shapeInput.property("value");
    console.log(shapeInputValue);
    console.log(tableData);
    var filteredData4 = tableData.filter(tableData => tableData.shape === shapeInput);
    buildTable(filteredData4);
  });

function buildTable(filteredShapeTable) {
    filteredData4.forEach((shapeData) => {
        var row = tbody.append("tr");
        Object.entries(shapeData).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });
};
