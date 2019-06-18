
# I. TỔNG QUAN

## 1.1. Đặt vấn đề

Với sự phát triển vượt bậc của công nghệ thông tin đặc biệt là sự bùng nổ của mạng internet, lượng thông tin được số hóa và đưa lên mạng ngày càng nhiều. Internet trở thành một kho kiến thức khổng lồ về mọi lĩnh vực. Do đó, số lượng văn bản xuất hiện trên mạng internet cũng tăng theo với tốc độ chóng mặt. Số lượng trang web cũng như lượng thông tin đang tăng một cách rất nhanh, đặc biệt với những bài báo điện tử. Với nhu cầu thực tế của người sử dụng, tìm kiếm thông tin nội dung liên quan đến những chủ đề lĩnh vực quan tâm vẫn còn là một thách thức to lớn. Làm thế nào để tìm kiếm chính xác, làm thế nào để phân loại các thông tin theo chủ đề để dễ dàng truy xuất và phân tích nội dung phục vụ cho việc thống kê, nghiên cứu dự đoán dựa trên những thông tin được phân loại đó.

Để giải quyết vấn đề, một phương pháp hoặc một hệ thống để phân loại tin tức được tổng hợp từ các trang báo điện tử là hết sức cần thiết.

## 1.2. Các phương pháp phân loại văn bản

Mỗi phương pháp phân loại văn bản đều có cách tính toán khác nhau. Nhìn một cách tổng quan thì các phương pháp đều thực hiện một số bước chung như sau: đầu tiên, mỗi phương pháp sẽ dựa trên các thông tin về sự xuất hiện của từ trong văn bản (ví dụ tần số, số văn bản chứa từ...) để biểu diễn văn bản thành dạng vector; sau đó, tuỳ từng phương pháp mà ta sẽ áp dụng công thức và phương thức tính toán khác nhau để thực hiện việc phân loại.

Phân loại văn bản tự động trong tiếng Anh đã có rất nhiều công trình nghiên cứu và đạt được kết quả đáng khích lệ. Dựa trên các thống kê của Yang & Xiu (1999), một số phương pháp phân loại thông dụng hiện nay là: Support Vector Machine [Joachims, 1998], k-Nearest Neighbor [Yang, 1994], Linear Least Squares Fit [Yang and Chute, 1994] Neural Network [Wiener et al, 1995], Naïve Bayes [Baker and Mccallum, 2000], Centroid-based [Shankar and Karypis, 1998]. Các phương pháp trên đều dựa vào xác suất thống kê hoặc thông tin về trọng số của từ trong văn bản.

Đối với tiếng Anh, các kết quả trong lĩnh vực này rất khả quan, còn đối với tiếng Việt, các công trình nghiên cứu về phân loại văn bản gần đây đã có một số kết quả ban đầu nhưng vẫn còn nhiều hạn chế. Nguyên nhân là ngay ở bước đầu tiên, chúng
ta đã gặp khó khăn trong việc xử lý văn bản để rút ra tần số xuất hiện của từ. Trong khi đó, để phân loại văn bản thì có thể nói bước đầu tiên là quan trọng nhất bởi vì nếu ở bước tách từ đã sai thì việc phân loại hầu như không thể thành công được.

## 1.3. Tách từ Tiếng Việt

Đối với tiếng Anh, từ là một nhóm các ký tự có nghĩa được tách biệt với nhau
bởi khoảng trắng trong câu, do vậy việc tách từ trở nên rất đơn giản. Trong khi đối với tiếng Việt, ranh giới từ không được xác định mặc định là khoảng trắng mà tùy thuộc vào ngữ cảnh dùng câu tiếng Việt. Ví dụ các từ trong tiếng Anh là “book”, “cat”, “stadium” thì trong tiếng Việt là “quyển sách”, “con mèo”, “sân vận động”,... Vấn đề trên thực sự đưa ra một thách thức to lớn.

Gần đây, một phương pháp tách từ mới được giới thiệu có ưu điểm là không cần dùng tập ngữ liệu hay từ điển để lấy thông tin thống kê hay trọng số của từ, đó là phương pháp Internet and Genetics Algorithm-based Text Categorization (IGATEC) của H.Nguyen et al (2005). Điểm sáng tạo của thuật toán là kết hợp thuật toán di truyền với việc trích xuất thông tin thống kê từ Internet thông qua một công cụ tìm kiếm (như Google chẳng hạn) thay vì lấy từ tập ngữ liệu như các phương pháp trước.

## 1.4. Mục tiêu đồ án

Trong pham vi đồ án này, nhóm sẽ tập trung tìm hiểu về cách thức phân loại văn bản trong Tiếng Việt cụ thể là phân loại các bài báo tin tức được lấy từ các trang báo điện tử lớn ở Việt Nam.

Song song đó, nhóm cũng tìm hiểu ở mức cơ bản một số phương pháp phân loại văn bản hiện có đang áp dụng cho tiếng Anh như Support vector Machine (SVM), K–Nearest Neighbor (kNN) và Naïve Bayes (NB) để có cái nhìn tổng quan và cơ bản nhất.

Cuối cùng sẽ áp dụng phương pháp Naïve Bayes để giải quyết bài toán phân loại bài báo trong Tiếng Việt, từ việc thu thập dữ liệu trên internet, rồi đến làm sạch dữ liệu, tiền xử lý dữ liệu, rút trích đặc trưng, tách từ, áp dụng model, training model và cuối cùng là đưa ra nhận xét và đánh giá.

# II. CÁC PHƯƠNG PHÁP PHÂN LOẠI VĂN BẢN TIẾNG ANH

## 2.1. Tổng quan về các phương pháp phân loại văn bản hiện nay

Để phân loại văn bản người ta sử dụng nhiều cách tiếp cận khác nhau như dựa trên từ khóa, dựa trên ngữ nghĩa các từ có tần số xuất hiện cao, mô hình Maximum Entropy, tập thô... Tiếng Anh là một trong những ngôn ngữ được nghiên cứu sớm và rộng rãi nhất với kết quả đạt được rất khả quan. Một số lượng lớn các phương pháp phân loại đã được áp dụng thành công trên ngôn ngữ này : mô hình hồi quy [Fuhr et al,1991], phân loại dựa trên láng giềng gần nhất (k-nearest neighbors) [Dasarathy, 1991], phương pháp dựa trên xác suất Naïve Bayes [Joachims, 1997], cây quyết định [Fuhr et al,1991], học luật quy nạp [William & Yoram, 1996], mạng nơron (neural network) [Wiener et al, 1995], học trực tuyến[William & Yoram, 1996], và máy vector hỗ trợ (SVM-support vector machine) [Vapnik, 1995]. Hiệu quả của các phương pháp này rất khác nhau ngay cả khi áp dụng cho tiếng Anh. Việc đánh giá gặp nhiều khó khăn do việc thiếu các tập ngữ liệu huấn luyện chuẩn. Thậm chí đối với tập dữ liệu được sử dụng rộng rãi nhất, Reuter cũng có nhiều phiên bản khác nhau. Hơn nữa, có rất nhiều độ đo được sử dụng như recall,
precision, accuracy hoặc error, break-even point, F-measure... Chương này giới thiệu các thuật toán phân loại được sử dụng phổ biến nhất đồng thời so sánh giữa các phương pháp sử dụng kết quả của [Yang, 1997].

## 2.2. Một số phương pháp phân loại văn bản tiếng Anh hiện hành

### 2.2.1. Support vector Machine (SVM)

SVM là phương pháp tiếp cận phân loại rất hiệu quả được Vapnik giới thiệu năm 1995 [Vapnik, 1995] để giải quyết vấn đề nhận dạng mẫu 2 lớp sử dụng nguyên lý Cực tiểu hóa Rủi ro có Cấu trúc (Structural Risk Minimization) [Vapnik, Cortes, 1995].

#### 2.2.1.1 Ý tưởng

Cho trước một tập huấn luyện được biểu diễn trong không gian vector trong đó mỗi tài liệu là một điểm, phương pháp này tìm ra một siêu mặt phẳng h quyết định tốt nhất có thể chia các điểm trên không gian này thành hai lớp riêng biệt tương ứng
lớp + và lớp –. Chất lượng của siêu mặt phẳng này được quyết định bởi khoảng cách (gọi là biên) của điểm dữ liệu gần nhất của mỗi lớp đến mặt phẳng này. Khoảng cách biên càng lớn thì mặt phẳng quyết định càng tốt đồng thời việc phân loại càng chính xác. Mục đích thuật toán SVM tìm được khoảng cách biên lớn nhất. Hình sau minh họa cho thuật toán này:

<img src="./assets/svm-repport.png">

[Siêu mặt phẳng h phân chia dữ liệu huấn huyện thành 2 lớp + và – với khoảng cách biên lớn nhất. Các điểm gần h nhất là các vector hỗ trợ, Support Vector (được khoanh tròn)]

#### 2.2.1.2 Công thức

SVM thực chất là một bài toán tối ưu, mục tiêu của thuật toán này là tìm được một không gian H và siêu mặt phẳng quyết định trên H sao cho sai số phân loại là thấp nhất.

Phương trình siêu mặt phẳng chứa vector d(i) trong không gian như sau: d(i).w + b = 0

Bài toán SVM có thể giải bằng kỹ thuật sử dụng toán tử Lagrange để biến đổi thành dạng đẳng thức. Điểm thú vị ở SVM là mặt phẳng quyết định chỉ phụ thuộc vào các vector hỗ trợ (Support Vector) có khoảng cách đến mặt phẳng quyết định là 1/|w|. Khi các điểm khác bị xóa đi thì thuật toán vẫn cho kết quả giống như ban đầu. Chính đặc điểm này làm cho SVM khác với các thuật toán khác như kNN,LLSF, NNet và NB vì tất cả dữ liệu trong tập huấn luyện đều được dùng để tối ưu hóa kết quả.

### 2.2.2. K–Nearest Neighbor (kNN)

kNN là phương pháp truyền thống khá nổi tiếng về hướng tiếp cận dựa trên thống kê đã được nghiên cứu trong nhận dạng mẫu hơn bốn thập kỷ qua [Dasarathy, 1991]. kNN được đánh giá là một trong những phương pháp tốt nhất (áp dụng trên tập dữ liệu Reuters phiên bản 21450), được sử dụng từ những thời kỳ đầu của việc phân loại văn bản [Marsand et al, 1992] [Yang, 1994] [Iwayama, Tokunaga, 1995].

#### 2.2.2.1 Ý tưởng

Khi cần phân loại một văn bản mới, thuật toán sẽ tính khoảng cách (khoảng cách Euclide, Cosine ...) của tất cả các văn bản trong tập huấn luyện đến văn bản này để tìm ra k văn bản gần nhất (gọi là k “láng giềng”), sau đó dùng các khoảng cách này
đánh trọng số cho tất cả chủ đề. Trọng số của một chủ đề chính là tổng tất cả khoảng cách ở trên của các văn bản trong k láng giềng có cùng chủ đề, chủ đề nào không xuất hiện trong k láng giềng sẽ có trọng số bằng 0. Sau đó các chủ đề sẽ được
sắp xếp theo mức độ trọng số giảm dần và các chủ đề có trọng số cao sẽ được chọn là chủ đề của văn bản cần phân loại.

#### 2.2.2.2 Công thức

Trọng số của chủ đề c(j) đối với văn bản x:

<img src="./assets/knn.png">

Để chọn được tham số k tốt nhất cho việc phân loại, thuật toán phải được chạy thử nghiệm trên nhiều giá trị k khác nhau, giá trị k càng lớn thì thuật toán càng ổn định và sai sót càng thấp [Yang, 1997]. Giá trị tốt nhất được sử dụng tương ứng trên hai bộ dữ liệu Reuter và Oshumed là k = 45 [Joachims, 1997].

### 2.2.3. Naïve Bayes (NB)

NB là phương pháp phân loại dựa vào xác suất được sử dụng rộng rãi trong lĩnh vực máy học [Mitchell, 1996] [Joachims, 1997] [Jason, 2001] được sử dụng lần đầu tiên trong lĩnh vực phân loại bởi Maron vào năm 1961 [Maron, 1961] sau đó trở nên phổ biến dùng trong nhiều lĩnh vực như trong các công cụ tìm kiếm [Rijsbergen et al, 1970], các bộ lọc mail [Sahami et al, 1998].

#### 2.2.3.1 Ý tưởng

Naive Bayes Classifier (NBC) là một thuật toán phân loại dựa trên tính toán xác suất áp dụng định lý Bayes. Thuật toán này thuộc nhóm Supervised Learning (Học có giám sát). Đây là hướng tiếp cận phân lớp theo mô hình xác suất. Dự đoán xác suất một đối tượng mới thuộc về thành viên của lớp đang xét.

Định lý Bayes là một định lý toán học để tính xác suất xảy ra của một sự kiện ngẫu nhiên A khi biết sự kiện liên quan B đã xảy ra. Định lý này đặt theo tên nhà toán học Thomas Bayes, người Anh sống ở thế kỷ 18. Đây là một trong những công cụ vô cùng hữu ích, người bạn thân của các Data Scientist, những người làm trong ngành khoa học dữ liệu.

Ý tưởng cơ bản của cách tiếp cận Naïve Bayes là sử dụng xác suất có điều kiện giữa từ và chủ đề để dự đoán xác suất chủ đề của một văn bản cần phân loại. Điểm quan trọng của phương pháp này chính là ở chỗ giả định rằng sự xuất hiện của tất cả các từ trong văn bản đều độc lập với nhau. Như thế NB không tận dụng được sự phụ thuộc của nhiều từ vào một chủ đề cụ thể.

Giả định đó làm cho việc tính toán NB hiệu quả và nhanh chóng hơn các phương pháp khác với độ phức tạp theo số mũ vì nó không sử dụng việc kếp hợp các từ để đưa ra phán đoán chủ đề.

#### 2.2.3.2 Công thức

Theo định lý Bayes, ta có công thức tính xác suất ngẫu nhiên của sự kiện *Y* khi biết *X* như sau:  
<img src="./assets/CT-1.png">  
Giả sử ta phân chia 1 sự kiện *X* thành *n* thành phần khác nhau *X1, X2, ..., Xn*. Naive Bayes theo đúng như tên gọi dựa vào một giả thiết ngây thơ rằng *X1, X2, ..., Xn* là các thành phần độc lập với nhau. Từ đó ta có thể tính được:  
<img src="./assets/CT-2.png">  
Do đó ta có:  
<img src="./assets/CT-3.png">  
Trên thực tế thì ít khi tìm được dữ liệu mà các thành phần là hoàn toàn độc lập với nhau. Tuy nhiên giả thiết này giúp cách tính toán trở nên đơn giản, training data nhanh, đem lại hiệu quả bất ngờ với các lớp bài toán nhất định.  

# III. CÁC PHƯƠNG PHÁP TÁCH TỪ TIẾNG VIỆT HIỆN NAY

## 3.1. Tổng quan về các phương pháp tách từ Tiếng Việt

So với Tiếng Anh, tách từ trong Tiếng Việt có nhiều điểm khác, dưới đây là bản so sánh qua nhiều điểm được tổng hợp dựa trên bảng công bố của [Đinh Điền, 2004].

| Đặc điểm của Tiếng Việt                                                                                                                                                      | Đặc điểm của Tiếng Anh                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Được xếp là loại hình đơn lập (isolate) hay còn gọi là loại hình phi hình thái, không biến hình, đơn tiết.                                                                   | Là loại hình biến cách (flexion) hay còn gọi là loại hình khuất chiết.                                                                      |
| Từ không biến đổi hình thái, ý nghĩa ngữ pháp nằm ở ngoài từ. Ví dụ : Chị ngã em nâng và Em ngã chị nâng.                                                                    | Từ có biến đổi hình thái, ý nghĩa ngữ pháp nằm ở trong từ. Ví dụ: I see him và He sees me.                                                  |
| Phương thức ngữ pháp chủ yếu: trật tự từ và hư từ.                                                                                                                           | Phương thức ngữ pháp chủ yếu là : phụ tố.                                                                                                   |
| Ví dụ: Gạo xay và Xay gạo; đang học và học rồi; “nó bảo sao không tới”, “sao không bảo nó tới”, “sao không tới bảo nó”...                                                    |                                                                                                                                             |
| Ranh giới từ không được xác định mặc nhiên bằng khoảng trắng                                                                                                                 | Kết hợp giữa các hình vị là chặt chẽ, khó xác định, được nhận diện bằng khoảng trắng hoặc dấu câu.                                          |
| Tồn tại loại từ đặc biệt “từ chỉ loại” (classifier) hay còn gọi là phó danh từ chỉ loại kèm theo với danh từ, như: cái bàn, cuốn sách, bức thư, con chó, con sông, vì sao... | Hiện tượng cấu tạo bằng từ ghép thêm phụ tố (affix) vào gốc từ là rất phổ biến. Ví dụ: anticomputerizational (anti-compute-er-ize-ation-al) |
| Có hiện tượng láy và nói lái trong tiếng Việt. Ví dụ: lấp lánh, lung linh, hiện đại -> hại điện, thầy giáo -> tháo giầy...                                                   |                                                                                                                                             |

Như vậy:

Tiếng Việt là loại hình phi hình thái nên việc phân biệt loại từ (danh từ, động từ, tính từ ...) và ý nghĩa từ là rất khó, cho dù có sử dụng từ điển.

Việc tiền xử lý văn bản (tách từ, tách đoạn, tách câu...) sẽ thêm phức tạp với phần xử lý các hư từ, phụ từ, từ láy.

Phương thức ngữ pháp chủ yếu là trật tự từ nên nếu áp dụng phương pháp tính xác suất xuất hiện của từ có thể không chính xác như mong đợi.

Ranh giới từ không được xác định mặc nhiên bằng khoảng trắng. Điều này khiến cho việc phân tích hình thái (tách từ) tiếng Việt trở nên khó khăn. Việc nhận diện ranh giới từ là quan trọng làm tiền đề cho các xử lý tiếp theo sau đó, như: kiểm lỗi chính tả, gán nhãn từ loại, thống kê tần suất từ.

Vì giữa tiếng Anh và tiếng Việt có nhiều điểm khác biệt nên chúng ta không thể áp dụng y nguyên các thuật toán tiếng Anh cho tiếng Việt.

## 3.2. Một số phương pháp tách từ

### 3.2.1. Các hướng tiếp cận dựa trên từ (Word-based approaches)

### 3.2.2. Các hướng tiếp cận dựa trên ký tự (Character-based approaches)

# IV. BÀI TOÁN PHÂN LOẠI TIN TỨC

## 4.1. Lý do chọn phương pháp Naïve Bayes

## 4.2. Thu thập dữ liệu và làm sạch dữ liệu (Raw Data và Clean Data)

## 4.3. Trích xuất đặc trưng (Feature Extraction)

## 4.4. Phân lớp văn bản (Implement Model và Train Model)

## 4.5. Đánh giá và kết luận

## 4.6. Môi trường triển khai

# V. Kết quả và hướng phát triển

## 5.1 Kết quả đạt được

## 5.2 Hướng phát triển
