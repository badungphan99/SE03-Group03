[![Build Status](https://travis-ci.com/badungphan99/SE03-Group03.svg?branch=master)](https://travis-ci.com/badungphan99/SE03-Group03)
# Openschool

repo của nhóm 3 lớp công nghệ phần mềm SE03 hiện tại đang trong giai đoạn bàn bạc và đưa ra ý kiến nên tạm thời không có gì ở đây hết

## Mục tiêu, định hướng, các kết quả cần đạt

Tạo ra một nền tảng cho phép người dùng có thể tạo lớp học, chia sẻ tài liệu, diễn đàn để có thể trao đổi và học tập. 
  
## Công nghệ và công cụ

- Python3
- Flask
- SQLAlchemy
- PHP
- Yii
- Docker

## Chức năng chính

### Người dùng

- Giáo viên: cần xác minh danh tính, được tạo hoặc tham gia dạy các khóa học, đăng bài học trong những khóa học đã tạo hoặc tham gia
- Học sinh, sinh viên và những người khác được đăng kí học các khóa học. Đối với học sinh, sinh viên sau khi xác minh danh tính sẽ có nhiều ưu tiên hơn
- Admin: người kiểm soát việc xác minh danh tính của các tài khoản, kiểm duyệt các khóa học được tạo, các bài học, bài đăng, comment trong diễn đàn. Nếu phát hiện trường hợp vi phạm thì xóa bài và vô hiệu hóa tài khoản

### Khóa học

- Gồm tiêu đề, thể loại, mô tả, ngày tạo, thời lượng, giáo viên, số lượng người đăng kí học, các bài học
- Cuối mỗi bài học có phần quiz, nguời học làm bài và được chấm điểm, người học có thể xem lại điểm của từng bài quiz và điểm cả khóa học
- Sau khi xem tất cả các bài học và làm hết các bài quiz đạt ngưỡng điểm yêu cầu, người học được tính là đã hoàn thành khóa học
- Mỗi khóa học có một diễn đàn riêng để trao đổi, trong diễn đàn đó những người tham gia khóa học có thể đăng bài, xem, comment, like bài viết và like comment

### Bài viết

- Gồm tiêu đề, thể loại, ngày viết, nội dung, có phần comment, like
- Mọi người đã đăng kí tài khoản đều có thể tạo bài viết riêng để chia sẻ kiến thức.
- Bài viết sau khi được Admin kiểm duyệt và đạt yêu cầu sẽ được đăng vào mục blog để tất cả mọi người có thể xem được

## Cài đặt

- docker https://docs.docker.com/install/
- docker-compose https://docs.docker.com/compose/install/
- `$ docker-compose up -d`
- docker cho môi trường python chưa có

## Thành viên nhóm

- Phan Bá Dũng
- Nguyễn Thị Kim Cúc
- Phạm Thi Thu Hạnh
- Nguyễn Việt Hoàng 
   
