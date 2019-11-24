var open 			= document.getElementById("btn-open-bar");
var nav 			= document.getElementById("nav");

open.addEventListener("click", ControlNav);
// CloseEditFramesm.addEventListener("click", ClosePanelEditsm);
var numControlNav = 0;

function ControlNav() {
   if(numControlNav == 0){
      console.log(numControlNav);
      nav.style.display = "block";
      numControlNav = 1;
   }else{
      
      console.log(numControlNav);
      nav.style.display = "none";
      numControlNav = 0;
   }
}