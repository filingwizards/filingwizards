var piechart = {
	type: 'pie',
	data: {
		datasets: [
			{
				data: [40, 25, 35],
				backgroundColor: [
					"#f7be68",
					"#fe6c61",
					"#5472d2",
				],
			},
			{
				data: [],
				backgroundColor: [
					"transparent",
					"transparent",
					"transparent",
				],
			}
		],
		labels: [
			"Stock",
			"Bound",
			"Fund",
		]
	},
	options: {
		responsive: true,
		title: {
			display: false
		},
		legend: {
			display: true,
			position: 'right',
		},
	}
};

window.onload = function() {
	var ctx = document.getElementById("piechart").getContext("2d");
	window.myPie = new Chart(ctx, piechart);
};