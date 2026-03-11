chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

if(changeInfo.status === "complete"){

let url = tab.url;

fetch("http://127.0.0.1:5000/predict",{

method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
url:url
})

})
.then(response => response.json())
.then(data => {

console.log("Detection Result:",data.result)

if(data.result.includes("Phishing")){

alert("⚠️ Warning! Possible phishing website detected!")

}

});

}

});
