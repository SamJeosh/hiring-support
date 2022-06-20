let btn = document.getElementById("Calc");
let c_Comm= document.getElementById("c_Comm");
let c_Con= document.getElementById("c_Con");
let c_Tech= document.getElementById("c_Tech");
let c_Employ = document.getElementById("c_Employ");
let fin = document.getElementById("c_final_score");

function deleteNote(noteId){
	fetch("/delete-note", {
		method : "POST",
		body : JSON.stringify({noteId : noteId}),
	}).then((_res)=>{
		window.location.href = "/";
	});
}




btn.onclick = function(){
	let A = parseInt(c_Comm.value)
	let B = parseInt(c_Con.value)
	let C = parseInt(c_Tech.value)
	let D = parseInt(c_Employ.value)

	let T =(A + B + C + D)/10
    fin.value = T;

}