function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // $.post("login",
    // {
    //   username: username,
    //   password: password
    // },
    // function(data,status){
    //   data1 = data;
    //   status1 = status;
    //   alert("Data: " + data + "\nStatus: " + status);
    //     window.location = "block_home.html";
    // });
    // alert("Data: " + data1 + "\nStatus: " + status1);
    // window.location = "block_home.html";
    // return true;
}

//show/hide pass
function myFunction(){
    var x = document.getElementById("myInput");
    if (x.type === "password"){
        x.type = "text"
    } else {
        x.type = "password";
    }
}
$(".toggle-password").click(function () {
    $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "password") {
        input.attr("type", "text");
    } else {
        input.attr("type", "password");
    }
});