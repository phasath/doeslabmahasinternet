async function insertTableData(jsonRes){
	$("#tableContent tr").remove();
	const header = Object.keys(jsonRes.header)
	header.unshift('timestamp')
	const rows = jsonRes.data

	for (let row of rows){
		let rowText = ''
		for (let el of header){
			rowText += `<td>${row[el]}</td>`
		}
		$('#tableContent').find('tbody').append(`<tr>${rowText}</tr>`);
	}
}

async function insertHeaderData(res){
	$("#tableHeader tr").remove();
	let headers = ''
	headers = `<th>Timestamp</th>`
	for (let [key, value] of Object.entries(res)){
		headers += `<th><a href='${value}'>${key}</a></th>`
	}
	$('#tableHeader').find('thead').append(`<tr>${headers}</tr>`);
}

function loadData(limit=10){
	$('#loader').addClass('loader').attr("hidden",false)
	$.get(`/history/fetch?limit=${limit}`, async (data) => {
		const jsonRes = JSON.parse(data)
		const headerPromise = insertHeaderData(jsonRes.header)
		const dataPromise = insertTableData(jsonRes)
		await Promise.all([headerPromise, dataPromise])
	}).then(()=>{
		$('#result').attr('hidden', false)
		$('#loader').removeClass('loader').attr('hidden', true)
	}

	);
}

$(document).ready(async function() {
	loadData(10);
});
