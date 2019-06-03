# Implement Text Classification

## Tools

- GenSim : https://studylinux.wordpress.com/2017/11/03/7-librarytool-nen-biet-khi-bat-dau-machine-learningdeep-learning-tren-python/#more-2612

- Dataset: https://github.com/duyvuleo/VNTC/blob/master/Data/10Topics/Ver1.1/Stats.txt

- Vitk -- A Vietnamese Text Processing Toolkit https://github.com/phuonglh/vn.vitk
- VnCoreNLP: A Vietnamese natural language processing toolkit https://github.com/vncorenlp/VnCoreNLP

### Bài hướng dẫn

- Bài toán về ứng dụng Naive Bayes sử dụng Bow trong phân loại, có code demo: https://viblo.asia/p/ung-dung-naive-bayes-vao-phan-loai-bai-bao-Ljy5VM2jlra
- Bài hướng dẫn về phân loại bài viết Tiếng Việt: https://viblo.asia/p/phan-loai-van-ban-tieng-viet-tu-dong-phan-1-yMnKM3bal7P

### Các ghi chú

Các yếu tố ảnh hưởng đến độ chính xác của bài toán:

- Tách từ   -> yêu cầu 1 phương pháp tách từ chuẩn xác.
- Vertor hóa    -> BoW xóa bỏ những chiều vertor có trọng số là 0 để giảm số chiều -> áp dụng đánh trọng số TF-IDF.
- Train ML model -> Dùng model phù hợp, tinh chỉnh HyperParemeter cho hợp lý. (có thể chạy thủ công bằng tay, hoặc thư viện hổ trợ dò tìm, có thể biểu diễn theo đồ thị để xem điểm đạt giá trị cao nhất).
- Predict, data_test phải đưa về vertor và phải cùng số chiều của data_train rồi đưa vào model đã được trainning.
- Model sao khi train xong sẽ có "hình dạng" như thế nào? Nó được biểu diễn theo đúng mô tả thuật toán machine learning sử dụng tạo ra model đó.
- Các số HyperParemeter của mỗi thuật toán khác nhau và mỗi số sẽ có ý nghĩa riêng của nó -> tìm hiểu về thuật toán Naive Bayes.
