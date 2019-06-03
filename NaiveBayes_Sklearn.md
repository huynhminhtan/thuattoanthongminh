# Thuật toán Naive Bayes dùng trong Text Classification với thư viện Scikit-learn

## I. Thư viện Scikit-learn  

Scikit-learn (viết tắt là Sklearn) là một thư viện mã nguồn mở dành cho Machine Learning - một ngành trong trí tuệ nhân tạo, rất mạnh mẽ và thông dụng với cộng đồng Python, được thiết kế trên nền NumPy và SciPy. Scikit-learn chứa hầu hết các thuật toán Machine Learning hiện đại nhất, đi kèm với documentations luôn được cập nhật.  

Tại sao chọn thư viện Scikit-learn để giải quyết bài toán này?  

- Hỗ trợ hầu hết các thuật toán của Machine Learning một cách đơn giản, hiệu quả mà chúng ta không cần phải mất công ngồi cài đặt lại. Scikit-learn có hỗ trợ 4 loại thuật toán của Naive Bayes: Gaussian Naive Bayes, Multinomial Naive Bayes, Complement Naive Bayes, Bernoulli Naive Bayes. Tùy vào loại dữ liệu của bài toán cần giải quyết mà lựa chọn loại thuật toán Naive Bayes thích hợp. Với bài toán của mình, chúng ta sẽ dùng Multinomial Naive Bayes. 
- Có tài liệu hướng dẫn sử dụng.
- Độ tin cậy cao do Scikit-learn được xây dựng bởi các chuyên gia hàng đầu.
- Có nguồn dữ liệu phong phú: iris, digit, …

## II. Thuật toán Naives Bayes  

References:  

1. https://scikit-learn.org/stable/modules/naive_bayes.html  

2. https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB  

3. https://scikit-learn.org/stable/modules/classes.html#module-sklearn.naive_bayes  