function getData(){
	fetch(`/graphics/${filename}`)
		.then(response => response.json())
		.then(data => {
		console.log(data)
		for(var i = 0;i < data.length;i++){
			console.log(data[i])
			var datos = data[i]
		return datos
		}
		})
	
}
// Our labels along the x-axis
var ejex = datos['datos_header'];
// For drawing the lines
var ejey = datos['datos_body'];
var asia = [282,350,411,502,635,809,947,1402,3700,5267];
var europe = [168,170,178,190,203,276,408,547,675,734];
var latinAmerica = [40,20,10,16,24,38,74,167,508,784];
var northAmerica = [6,3,2,2,7,26,82,172,312,433];

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ejex,
    datasets: [
        { 
            data: ejey,
            label: "Ejey",
            borderColor: "#3e95cd",
            fill: false
          },
          { 
            data: asia,
            label: "Asia",
            borderColor: "#3e95cd",
            fill: false
          },
          { 
            data: europe,
            label: "Europe",
            borderColor: "#3e95cd",
            fill: false
          },
          { 
            data: latinAmerica,
            label: "Latin America",
            borderColor: "#3e95cd",
            fill: false
          },
          { 
            data: northAmerica,
            label: "North America",
            borderColor: "#3e95cd",
            fill: false
          }
    ]
  }
});