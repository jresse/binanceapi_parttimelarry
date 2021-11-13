var chart = LightweightCharts.createChart(document.body, {
	width: 1000,
  height: 500,
	// layout: {
	// 	backgroundColor: '#000000',
	// 	textColor: 'rgba(255, 255, 255, 0.9)',
	// },
	// grid: {
	// 	vertLines: {
	// 		color: 'rgba(197, 203, 206, 0.5)',
	// 	},
	// 	horzLines: {
	// 		color: 'rgba(197, 203, 206, 0.5)',
	// 	},
	// },
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	// rightPriceScale: {
	// 	borderColor: 'rgba(197, 203, 206, 0.8)',
	// },
	// timeScale: {
	// 	borderColor: 'rgba(197, 203, 206, 0.8)',
	// },
});

var candleSeries = chart.addCandlestickSeries(
// 	{
//   upColor: 'rgba(255, 144, 0, 1)',
//   downColor: '#000',
//   borderDownColor: 'rgba(255, 144, 0, 1)',
//   borderUpColor: 'rgba(255, 144, 0, 1)',
//   wickDownColor: 'rgba(255, 144, 0, 1)',
//   wickUpColor: 'rgba(255, 144, 0, 1)',
// }
);

fetch('http://localhost:5000/history')
	.then((r) => r.json())
	.then((response) => {
		console.log(response)
		candleSeries.setData(response);
	})


// const chart = LightweightCharts.createChart(document.getElementById('charts'), { width: 400, height: 300 });
// const lineSeries = chart.addLineSeries();
// lineSeries.setData([
//     { time: '2019-04-11', value: 80.01 },
//     { time: '2019-04-12', value: 96.63 },
//     { time: '2019-04-13', value: 76.64 },
//     { time: '2019-04-14', value: 81.89 },
//     { time: '2019-04-15', value: 74.43 },
//     { time: '2019-04-16', value: 80.01 },
//     { time: '2019-04-17', value: 96.63 },
//     { time: '2019-04-18', value: 76.64 },
//     { time: '2019-04-19', value: 81.89 },
//     { time: '2019-04-20', value: 74.43 },
// ]);

var coinSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_5m");
//console.log(coinSocket);

//var tradeDiv = document.getElementById("trades")
coinSocket.onmessage = function (event) {
// console.log(event.data);
//var messageObj = JSON.parse(event.data)
//tradeDiv.append(messageObj.p)
	var message = JSON.parse(event.data);
	console.log(message.k)
	var candlestick = message.k;

	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}
