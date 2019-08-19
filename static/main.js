var btn = document.getElementById("btn");
var container = document.getElementById("container");
var url = 'http://127.0.0.1:8000';

// Using jquery Ajax
$.ajax({
    method: 'GET',
    url: url,
    success: function(data){
        console.log(data);
        console.log("Success");
    },
    error: function (error_data) {
        console.log("Error");
    }
});


// Using vanilla javascript
btn.addEventListener("click", function () {
    var ourRquest = new XMLHttpRequest();
    ourRquest.open("GET", url);
    ourRquest.onload = function () {
        console.log(ourRquest.responseText);
        var ourData = JSON.parse(ourRquest.responseText);
        console.log(ourData)
    }
    ourRquest.send()
});