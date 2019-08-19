var btn = document.getElementById("btn");
var container = document.getElementById("container");
var url = 'http://127.0.0.1:8000';

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