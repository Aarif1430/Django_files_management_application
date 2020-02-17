var container = document.getElementById("ourcontainer");
var url = 'http://127.0.0.1:5000/documents/';

$.ajax({
	method: 'GET',
	url: url,
	success: function(data){
	    renderHTML(data)
		console.log(data)
		console.log("success")
	},
	error: function(error_data){
		console.log("error")
	}
})

function renderHTML(data) {
	var container = document.getElementById("document_container");
	var htmlString = "";

	for (i=0; i < data.documents.length; i++){

		htmlString += "<li><a href="+data.documents[i]["pdf"]+">" + data.documents[i]["pdf"]+"</a></li>";
	}

	container.insertAdjacentHTML('beforeend', htmlString);
}
