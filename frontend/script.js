const API_URL = "http://127.0.0.1:8000";

let textChart;
let urlChart;

/* =========================
   TAB SWITCHING
========================= */

function showTab(tab){

document.getElementById("textSection").style.display = "none";
document.getElementById("urlSection").style.display = "none";
document.getElementById("imageSection").style.display = "none";

document.getElementById("msgTab").classList.remove("active");
document.getElementById("urlTabBtn").classList.remove("active");
document.getElementById("imgTab").classList.remove("active");

if(tab === "text"){
document.getElementById("textSection").style.display = "block";
document.getElementById("msgTab").classList.add("active");
}
else if(tab === "url"){
document.getElementById("urlSection").style.display = "block";
document.getElementById("urlTabBtn").classList.add("active");
}
else{
document.getElementById("imageSection").style.display = "block";
document.getElementById("imgTab").classList.add("active");
}

}


/* =========================
   CHART (optional preview)
========================= */

function drawChart(id,value){

return new Chart(document.getElementById(id),{

type:'doughnut',

data:{
datasets:[{
data:[value,100-value],
}]
},

options:{
cutout:'75%',
plugins:{
legend:{display:false}
}
}

});

}


/* =========================
   TEXT ANALYSIS
========================= */

async function analyzeText(){

let message = document.getElementById("messageInput").value;

if(!message){
alert("Enter a message");
return;
}

let response = await fetch(API_URL + "/analyze-text",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:message
})

});

let data = await response.json();

/* SAVE RESULT */

localStorage.setItem("analysisResult", JSON.stringify(data));

/* REDIRECT */

window.location.href = "result.html";

}


/* =========================
   URL ANALYSIS
========================= */

async function analyzeURL(){

let url = document.getElementById("urlInput").value;

if(!url){
alert("Enter a URL");
return;
}

let response = await fetch(API_URL + "/analyze-url",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
url:url
})

});

let data = await response.json();

/* SAVE RESULT */

localStorage.setItem("analysisResult", JSON.stringify(data));

window.location.href = "result.html";

}


/* =========================
   IMAGE (SCREENSHOT) ANALYSIS
========================= */

async function analyzeImage(){

const file = document.getElementById("imageInput").files[0];

if(!file){
alert("Please upload an image");
return;
}

/* Show scanning message */

let preview = document.getElementById("ocrPreview");
preview.innerText = "Scanning image...";

/* OCR USING TESSERACT */

const { data: { text } } = await Tesseract.recognize(file, 'eng');

/* Show extracted text */

preview.innerText = "Extracted: " + text.substring(0,150);

/* SEND TO SAME TEXT MODEL */

let response = await fetch(API_URL + "/analyze-text",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:text
})

});

let data = await response.json();

/* SAVE RESULT */

localStorage.setItem("analysisResult", JSON.stringify(data));

/* REDIRECT */

window.location.href = "result.html";

}