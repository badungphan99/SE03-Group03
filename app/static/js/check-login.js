function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    //Set 1 Admin ảo để đăng nhập quản trị
    if (username == "giaovien" && password == "123456789") {
        alert("Success! Hello Teacher", "success");
        window.location = "block_home.html";
        return true;
    }
    if(username == "hocvien" && password == "123456789") {
        alert("Success! Hello Student", "success");
        window.location = "block_home.html"
        return true;
    }
    if(username == "admin" && password == "123456789") {
        alert("Success! Hello Admin", "success");
        window.location = "block_home.html"
        return true;
    }
    //Nếu không nhập gì mà nhấn đăng nhập thì sẽ báo lỗi
    if (username == "" && password == "") {
        alert("Bạn Chưa Nhập Thông Tin!", "Vui Lòng Kiểm Tra Lại", "warning");
        return false;
    }
    //Nếu không nhập tài khoản sẽ báo lỗi
    if (username == null || username == "") {
        alert("Bạn Chưa Nhập Tài Khoản", "Vui Lòng Kiểm Tra Tài Khoản", "error");
        return false;
    } 
    //Nếu không nhập mật khẩu sẽ báo lỗi
    if (password == null || password == "") {
        alert("Bạn Chưa Nhập Mật Khẩu", "Vui Lòng Kiểm Tra Mật Khẩu", "error");
        return false;
    }
    //Nếu mật khẩu dưới 8 ký tự 
    if (password.length < 9) {
        alert("Bạn Nhập Chưa Đủ Mật Khẩu", "Mật Khẩu Phải Đủ 9 Ký Tự Bao Gồm Chữ Và Số", "error");
        return false;
    }
    //Nếu mật khẩu trên 8 ký tự thì sẽ báo lỗi
    if (password.length > 9) {
        alert("Bạn Nhập Dư Mật Khẩu", "Vui Lòng Kiểm Tra Lại Mật Khẩu", "error");
        return false;
    }
    alert("Thông Tin Bạn Nhập Không Tồn Tại", "Vui Lòng Kiểm Tra Hoặc Nhấn Quên Mật Khẩu", "error");
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