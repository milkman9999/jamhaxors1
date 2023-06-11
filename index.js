// const jsdom = require("jsdom");
// const { JSDOM } = jsdom;
try {
var submitButton = document.getElementById("submit")
}

catch {
    console.log('could not find element')
}
document.getElementById("submit").addEventListener("click", buttonClicked)

function buttonClicked () {
    //console.log(document.getElementById('age'.textContent))
    var age = parseInt(document.getElementById("age").value);
    var weight = parseInt(document.getElementById("weight").value);
    var sex = document.getElementById("sex").value; 
    var time = document.getElementById("time").value;
    var goal = document.getElementById("goal").value;
}


