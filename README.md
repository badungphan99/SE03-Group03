[![Build Status](https://travis-ci.com/badungphan99/SE03-Group03.svg?branch=master)](https://travis-ci.com/badungphan99/SE03-Group03)
# Openschool


## 1. Mục tiêu, định hướng, các kết quả cần đạt

Tạo ra một nền tảng cho phép người dùng có thể tạo lớp học, chia sẻ tài liệu, diễn đàn để có thể trao đổi và học tập. 
  
## 2. Công nghệ và công cụ
### 2.1 Công nghệ
- Python3
- Flask
- SQLAlchemy
- Docker
- HTML, CSS, JavaScript, Bootstrap

### 2.2 Công cụ
- phpMyAdmin
- MySQL
- PyCharmIDE

## 3. Chức năng chính

### 3.1 Người dùng

- Giáo viên: cần xác minh danh tính, được tạo hoặc tham gia dạy các khóa học, đăng bài học trong những khóa học đã tạo hoặc tham gia
- Học sinh, sinh viên và những người khác được đăng kí học các khóa học. Đối với học sinh, sinh viên sau khi xác minh danh tính sẽ có nhiều ưu tiên hơn
- Admin: người kiểm soát việc xác minh danh tính của các tài khoản, kiểm duyệt các khóa học được tạo, các bài học, bài đăng, comment trong diễn đàn. Nếu phát hiện trường hợp vi phạm thì xóa bài và vô hiệu hóa tài khoản

### 3.2 Khóa học

- Gồm tiêu đề, thể loại, mô tả, ngày tạo, thời lượng, giáo viên, số lượng người đăng kí học, các bài học
- Cuối mỗi bài học có phần quiz, nguời học làm bài và được chấm điểm, người học có thể xem lại điểm của từng bài quiz và điểm cả khóa học
- Sau khi xem tất cả các bài học và làm hết các bài quiz đạt ngưỡng điểm yêu cầu, người học được tính là đã hoàn thành khóa học
- Mỗi khóa học có một diễn đàn riêng để trao đổi, trong diễn đàn đó những người tham gia khóa học có thể đăng bài, xem, comment, like bài viết và like comment

### 3.3 Bài viết

- Gồm tiêu đề, thể loại, ngày viết, nội dung, có phần comment, like
- Mọi người đã đăng kí tài khoản đều có thể tạo bài viết riêng để chia sẻ kiến thức.
- Bài viết sau khi được Admin kiểm duyệt và đạt yêu cầu sẽ được đăng vào mục blog để tất cả mọi người có thể xem được

## 4. Cài đặt

- `$ ./install_docker.sh`
- `$ ./build`

## 5. Cách sử dụng
  https://github.com/badungphan99/SE03-Group03/wiki

## 6. Thành viên nhóm

- Phan Bá Dũng
- Nguyễn Thị Kim Cúc
- Phạm Thi Thu Hạnh
- Nguyễn Việt Hoàng 
   
