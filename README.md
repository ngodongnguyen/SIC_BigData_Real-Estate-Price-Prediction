<h1>BÁO CÁO ĐỒ ÁN SIC - DỰ ĐOÁN GIÁ NHÀ ĐẤT</h1>
<h2>Cấu trúc folder đồ án</h2>
<h3>Gồm có 5 branches: Main, preprocessing, web_scraping, dev, deloy</h3>
<h4>Main</h4>
  
  - **App:** chứa trang **website** của dự án
  - **data:** chứa các dữ liệu về **bất động sản** và **đơn vị hành chính Việt Nam**
  - **Modules:** chứa file **code** về **web scraping**
  - **README.MD:** chứa báo cáo đồ án
  <h4>Preprocessing</h4>
  
  - Chứa các file **code** về tiền sử lý dữ liệu bao gồm từ đất, chung cư, nhà ở
<h4>Web_scraping</h4>
  
  - Chứa các mouules **code** về lấy dữ liệu các trang web sử dụng Selenium, Beautiful Soup, CloudScraper
<h4>Deploy</h4>
  
  - Chứa trang **website** của dự án
<h2>1. Thành viên nhóm</h2>

* Team size: 6
* Thành viên :
  * Bùi Nhật Huy
  * Nguyễn Quang Huy
  * Nguyễn Thị Kim Ngân
  * Ngô Đông Nguyên
  * Nguyễn Yến Nhi
  * Lê Công Quận
* Phân công:
    | Thành viên | Công việc |
    | ----------- | ----------- |
    | Bùi Nhật Huy | <ul> <li>Quản lý dự án, đảm bảo tiến độ</li><li>Thu thập dữ liệu </li><li>Phát triển mô hình dự đoán</li><li>Trực quan hóa dữ liệu</li></ul>  |
    | Nguyễn Quang Huy  | <ul><li>Thu thập dữ liệu </li><li>Phát triển web</li></ul> |
    | Nguyễn Thị Kim Ngân  | <ul><li>Biên soạn báo cáo dự án </li></ul> |
    | Ngô Đông Nguyên  | <ul><li>Thu thập dữ liệu </li><li>Trực quan hóa dữ liệu </li><li>Phát triển mô hình dự đoán </li></ul> |
    | Nguyễn Yến Nhi  | <ul><li>Thu thập dữ liệu </li><li>Biên soạn báo cáo dự án </li></ul> |
    | Lê Công Quận  | <ul><li>Thu thập dữ liệu </li><li>Trực quan hóa dữ liệu </li><li>Phát triển mô hình dự đoán </li></ul> |

<h2>2. Tổng quan đồ án</h2>

2.1. **Phát biểu đồ án**

- **Đồ án:** Dự đoán giá đất, nhà ở, chung cu với phạm vi trên toàn quốc với tập dữ liệu từ trang [Chợ tốt](https://nha.chotot.com/) và [Bất động sản](https://batdongsan.com.vn/)

2.2. **Quá trình thực hiện đồ án** : trải qua 4 giai đoạn khác nhau.

  - **Giai đoạn 1**: Ở giai đoạn này, nhóm hướng đến bài toán **dự đoán giá đất, chung cư và nhà ở** trên phạm vi **toàn quốc**. Sau đó, sử dụng các thư viện như là **Selenium, Beautiful Soup, CloudScraper** để thu thập dữ liệu từ trang [Chợ tốt](https://nha.chotot.com/) và [Bất động sản](https://batdongsan.com.vn/)

   <div style="text-align: center;">
    <strong>Chung cư</strong><br>
    <img src="https://github.com/user-attachments/assets/afd5f2f3-71e0-4780-901a-f4967f569d7e" alt="Dữ liệu về chung cư">
</div>
  <div style="text-align: center;">
    <strong>Nhà ở</strong><br>
    <img src="https://github.com/user-attachments/assets/f850a58d-ec11-4adb-b038-5e9594ab3cba" alt="Dữ liệu về nhà ở">
</div>
  <div style="text-align: center;">
    <strong>Đất</strong><br>
    <img src="https://github.com/user-attachments/assets/6f613e30-02dd-42ba-b476-16e149ba02f7" alt="Dữ liệu về đất">
</div>



- Vấn đề: Ở đây dữ liệu thiếu khá nhiều, và sẽ có một số cột không ảnh hưởng đến output giá chung cư nên sẽ phải tiền xử lý, trực quan hoá các cột dữ liệu để tìm ra dữ liệu nào được giữ lại để xây dựng cho quá trình traning ***(tiền xử lý sẽ được trình bày bên dưới)***
- **Giai đoạn 2**: Nhóm thực hiện tiền xử lý dữ liệu, đưa các dữ liệu chữ về thành số ví dụ như thành phố, quận sẽ về số hóa hết để dễ dàng mô hình hóa bài toán
- **Giai đoạn 3**: Nhóm thực hiện mô hình bài toán, phát hiện ra các outliner để có cái nhìn cũng như dự đoán phù hợp để sử dụng các mô hình học máy phù hợp
- **Giai đoạn 4**: Nhóm thực hiện học máy cho bài toán sử dụng các mô hình như là **Linear Regression**, **RandomForest**, **GBM**, ...
<h2>3. Phân tích chi tiết</h2>

**3.1. Đồ án:**
  
  - Dữ liệu sau khi thu thập được bao gồm :
    - 22827 dòng với dữ liệu của chung cư
    - 24205 dòng với dữ liệu của nhà ở
    - 16749 dòng với dữ liệu của đất

  - **Mô tả các biến**:
    - **DiaChi:** địa chỉ của chung cư, ở thành phố Hồ Chí Minh
    - **City:** Thuộc thành phố/tỉnh nào
    - **District**: Thuộc quận/huyện nào
    - **Ward**: Thuộc phường/xã nào
    - **MucGia:** giá bán.
    - **DienTich:** diện tích thực ở(sử dụng) trên sổ hồng, đơn vị: **triệu/m2**.
    - **PhapLy**: Hiện tại đã có sổ hay chưa
  - **Các biến khác của chung cư**:
    - **SoPhongNgu**: Số phòng ngủ của chung cư
    - **SoToilet**: Số toilet của chung cư
    - **NoiThat**: Tình trạng nội thất hiện tại
    - **Lat**: Vĩ độ
    - **Long**: Kinh độ
    - **HuongNha** : Hướng nhà của chung cư
    - **HuongBanCong**: Hướng ban công của chung cư
  - **Các biến khác của nhà ở**:
    - **SoPhongNgu**: Số phòng ngủ của nhà ở
    - **SoToilet**: Số toilet của nhà ở
    - **NoiThat**: Tình trạng nội thất hiện tại
    - **DuongVao**: Đường vào nhà rộng bao nhiêu mét
    - **SoTang**: Số tầng của nhà ở
    - **HuongNha** : Hướng nhà của nhà ở
  - **Các biến khác của đất**:
    - **MatTien**: Mặt tiền rộng bao nhiêu mét
    - **DuongVao**: Đường vào nhà rộng bao nhiêu mét
    - **Lat**: Vĩ độ
    - **Long**: Kinh độ
    
    <br>
- **Tiền xử lý dữ liệu:**
    - Chỉ lấy các dòng dữ liệu có dữ liệu về: diện tích, phòng ngủ, phòng tắm và giá. Và đổi giá tiền từ VNĐ sang USD (theo tỉ giá 1$ ~ 25000)
    - Cái nhìn tổng quan về data sau khi clean:![Dữ liệu về chung cư](https://github.com/user-attachments/assets/23d255a6-f4be-4cad-993e-b1f3debb4e4b)
    <br>
    
- **Trực quan hoá dữ liệu:**
  - Trực quan dữ liệu giá trị **dạng số** ![Chung cư](https://github.com/user-attachments/assets/d2448e83-6f06-4484-b468-02ba2bf43610)
  - 1. **Diện Tích vs logPrice:**
   - **Xu hướng:** Khi diện tích nhà tăng, giá (logPrice) cũng tăng, nhưng sự tăng này không đồng đều. Có một số nhà có diện tích nhỏ nhưng giá rất cao.

2. **Số Phòng Ngủ vs logPrice:**
   - **Xu hướng:** Số phòng ngủ không ảnh hưởng rõ ràng đến giá. Đa số nhà có từ 2 đến 4 phòng ngủ, nhưng giá có thể dao động rất nhiều ngay cả khi số phòng ngủ giống nhau.

3. **Số Toilet vs logPrice:**
   - **Xu hướng:** Tương tự như số phòng ngủ, số toilet cũng không ảnh hưởng rõ ràng đến giá. Các ngôi nhà có số lượng toilet khác nhau nhưng giá có thể dao động lớn.

### Tổng kết:
- **Diện Tích** có xu hướng tác động đến giá mạnh hơn so với số phòng ngủ và số toilet.
- **Số Phòng Ngủ** và **Số Toilet** có ít tác động rõ ràng đến giá
# Trực quan những categorical
![Chung Cư](https://github.com/user-attachments/assets/6df917c6-73b3-4434-b692-69a63732ad52)
### Phân tích biểu đồ:

Biểu đồ này so sánh mức giá nhà (Low, Medium, High) giữa các tỉnh và thành phố ở Việt Nam.

1. **Xu hướng chung:**
   - Các thành phố lớn như Hà Nội, TP. Hồ Chí Minh, và Đà Nẵng có mức giá nhà cao hơn so với các tỉnh khác, đặc biệt ở mức giá cao nhất (High).
   
2. **Những điểm đáng chú ý:**
   - **Thành phố Hà Nội và TP. Hồ Chí Minh:** Hai thành phố này có mức giá nhà cao nhất ở cả ba mức giá, đặc biệt là mức giá High.
   - **Một số tỉnh như Bình Dương, Hải Phòng, Bà Rịa - Vũng Tàu:** Có mức giá nhà khá đồng đều giữa ba mức giá, không có sự chênh lệch lớn.
   - **Tỉnh Hà Nam** Cũng có mức giá nhà Low cao hơn hẳn so với các tỉnh lân cận.
   - **Tỉnh Hưng Yên:** Cũng có mức giá nhà High cao hơn hẳn so với các tỉnh lân cận.


3. **Kết luận:**
   - **Khu vực đô thị lớn:** Các thành phố lớn như Hà Nội, TP. Hồ Chí Minh, và Đà Nẵng là nơi có giá nhà cao, đặc biệt ở mức giá cao nhất.
   - **Chênh lệch giá:** Một số tỉnh có sự chênh lệch lớn giữa các mức giá, điều này có thể phản ánh sự phân hóa trong phát triển kinh tế hoặc nhu cầu thị trường nhà ở.
   - **Sự ổn định:** Một số tỉnh có mức giá nhà khá đồng đều giữa các mức giá, có thể cho thấy sự ổn định hoặc ít biến động về thị trường nhà ở.

Biểu đồ này cung cấp cái nhìn tổng quát về sự phân bố giá nhà giữa các tỉnh và thành phố, giúp xác định những khu vực có giá nhà cao và sự chênh lệch giữa các mức giá.

![Chung cư](https://github.com/user-attachments/assets/6218e36a-dc27-4360-9b46-02871715f0f5)
![Chugn cư](https://github.com/user-attachments/assets/5e732aa2-2ac2-4f6c-8c84-4de1174243de)

### Phân tích giá nhà ở thủ đô Hà Nội:

 1. **Xu hướng chung:**
   - **Khu vực trung tâm:** Các quận trung tâm như Hoàn Kiếm, Ba Đình, Đống Đa, và Hai Bà Trưng thường có giá nhà cao nhất trong khu vực, đều đạt ở mức Medium và High. Điều này là do vị trí đắc địa, gần các trung tâm hành chính, văn hóa, và kinh tế của Hà Nội.
   - **Khu vực phát triển mới:** Các quận như Cầu Giấy, Tây Hồ, và Thanh Xuân đang trở thành điểm nóng về bất động sản, với giá nhà tăng đều đặn nhờ sự phát triển hạ tầng và nhu cầu ở cao. Đặc biệt ở quận Tây Hồ khi giá đạt ở mức High cao hơn cả các quận trong khu vực trung tâm
   - **Khu vực ngoại thành:** Các huyện ngoại thành như Chương Mỹ, Quốc Oai, Thạch Thất có giá nhà thấp hơn nhiều so với khu vực trung tâm. Tuy nhiên, các khu vực này đang phát triển nhanh chóng nhờ vào các dự án hạ tầng lớn, khiến giá nhà có xu hướng tăng trong những năm gần đây.

 2. **Những điểm nổi bật:**
   - **Quận Hoàn Kiếm:** Giá nhà ở đây thường cao nhất do đây là khu vực trung tâm lịch sử và văn hóa của Hà Nội, với các tuyến phố cổ, hồ Hoàn Kiếm, và nhiều cơ quan hành chính quan trọng.
   - **Quận Tây Hồ:** Khu vực gần Hồ Tây là một trong những nơi có giá nhà cao nhất Hà Nội, nhờ không gian sống thoáng đãng, gần hồ và nhiều khu vực tiện ích cao cấp.
   - **Quận Cầu Giấy:** Với sự phát triển nhanh chóng của cơ sở hạ tầng, đây là một trong những khu vực có mức tăng giá nhà nhanh nhất ở Hà Nội.

 3. **Kết luận:**
   - **Khu vực trung tâm:** Những quận trung tâm như Hoàn Kiếm, Ba Đình có giá nhà rất cao, phù hợp với những người có nhu cầu ở gần trung tâm hoặc đầu tư bất động sản.
   - **Khu vực phát triển:** Các quận như Cầu Giấy, Tây Hồ là những khu vực đang phát triển mạnh với tiềm năng tăng giá cao.
   - **Khu vực ngoại thành:** Các huyện ngoại thành có giá nhà thấp hơn nhưng tiềm năng tăng giá lớn, đặc biệt khi các dự án cơ sở hạ tầng hoàn thành có thể kể đến các huyện như là Gia Lâm, Hoài Đức
![Chugn cư](https://github.com/user-attachments/assets/4a3890ea-44c8-4cb0-88f3-15ff85a7e3a5)

### 1. **Nội thất và giá nhà:**
   - **Không nội thất (0):** 
     - Giá nhà ở mức Low và Medium tương đối đồng đều, có sự sụt giảm ở mức High
   - **Cao cấp (1):** 
     - Giá nhà cao nhất trong nhóm có nội thất cao cấp. Nội thất cao cấp thường đi kèm với các căn hộ hoặc nhà ở thuộc phân khúc hạng sang, ở 3 cột Low, Medium và High đều cao hơn so với 3 tình trạng nội thất còn lại.
   - **Đầy đủ | hoàn thiện (2):** 
     - - Giá nhà ở mức Low và Medium tương đối đồng đều, có sự tăng đáng kể ở mức High
   - **Cơ bản (3):** 
     - Giá nhà thuộc loại thất nhất trong 4 tình trạng nội thất, trong đó giá nhà sẽ tập trung chủ yếu ở phân khúc Medium
![Chung cư](https://github.com/user-attachments/assets/86b11507-e6d8-4d64-a32d-d61b95866c82)
![Chung cư](https://github.com/user-attachments/assets/b671d1ca-9107-4b76-800e-acf3c26e9c1b)
![Chung cư](https://github.com/user-attachments/assets/b5b98456-7833-4136-a47e-8117d93df4a6)
# Phân tích 3 biểu đồ

## **Phân tích chung về hướng ban công:**
   - **Hướng Đông Nam:**
     - Hướng Đông Nam được xem là hướng tốt trong phong thủy vì đón ánh sáng mặt trời buổi sáng mà không bị nóng như hướng Tây.
     - Giá nhà ở hướng Đông Nam thường cao hơn một chút so với các hướng khác, do đây là hướng được nhiều người ưa chuộng.

   - **Các hướng khác:**
     - Giá nhà ở các hướng khác có thể tương đối ổn định và không có sự chênh lệch lớn, vì các yếu tố về ánh sáng và phong thủy thường được cân nhắc nhưng không phải là yếu tố quyết định duy nhất.

### **Kết luận về hướng ban công:**
   - **Hướng Đông Nam là một trong những hướng được ưa chuộng nhất, dẫn đến sự chênh lệch giá đáng kể tùy thuộc vào loại hình nhà ở và vị trí.**
   - **Các yếu tố khác như phong thủy, tiện ích và vị trí đóng vai trò quan trọng trong việc xác định giá nhà, đặc biệt là với những căn nhà có hướng Đông Nam.**

## **Phân tích chung về hướng nhà:**
   - **Hướng Đông Bắc và Tây Bắc:**
     - **Phong thủy:** Hướng Đông Bắc thường được coi là hướng mang lại sự ổn định và sự hỗ trợ cho gia chủ trong nhiều khía cạnh của cuộc sống, bao gồm sự nghiệp và tài chính.
     - **Giá nhà:** Hướng Đông Bắc và Tây Bắc có thể trải dài từ phân khúc giá rẻ đến giá cao, tùy thuộc vào nhiều yếu tố như vị trí và loại hình nhà ở.

### **Kết luận về hướng nhà:**
   - **Hướng Đông Bắc và Tây Bắc có thể trải dài từ phân khúc giá rẻ đến giá cao.**
   - **Yếu tố phong thủy, tiện ích và vị trí đóng vai trò quan trọng trong việc xác định giá trị của căn nhà, đặc biệt đối với các hướng Đông Bắc và Tây Bắc.**

## **Phân tích chung về trạng thái pháp lý:**
   - **Không sổ (0):**
     - Giá nhà với trạng thái pháp lý "Không sổ" thường nằm trong khoảng từ 60,000 đến 200,000 đô la. 
     - Sự thiếu rõ ràng về pháp lý có thể làm giảm giá trị của căn nhà, nhưng nó có thể được bù đắp bằng các yếu tố khác như vị trí và loại hình nhà ở.

   - **Đã có sổ (1), Đang chờ sổ (2), Viết tay (4):**
     - Giá nhà với các trạng thái pháp lý này thường trải dài từ vài chục ngàn đô la đến vài trăm ngàn đô la.
     - Các trạng thái này đều được xem là có giá trị pháp lý tương đối ổn định và có thể được thị trường chấp nhận rộng rãi, vì vậy giá trị của căn nhà không bị ảnh hưởng quá nhiều bởi vấn đề pháp lý.

   - **Sổ chung / Công chứng vi bằng (3):**
     - Giá nhà với trạng thái pháp lý "Sổ chung / Công chứng vi bằng" thường nằm trong khoảng từ 50,000 đến 70,000 đô la.
     - Trạng thái pháp lý này có thể làm giảm giá trị của căn nhà so với các trạng thái pháp lý rõ ràng hơn, vì sự không rõ ràng trong sổ đỏ có thể gây ra rủi ro pháp lý cho người mua.

### **Kết luận:**
   - **Các trạng thái pháp lý "Đã có sổ", "Đang chờ sổ", và "Viết tay" thường có mức giá tương đối cao, trải dài từ vài chục ngàn đô la đến vài trăm ngàn đô la.**
   - **Trạng thái "Không sổ" có giá thấp hơn, từ 60,000 đến 200,000 đô la, trong khi "Sổ chung / Công chứng vi bằng" có giá thấp nhất, từ 50,000 đến 70,000 đô la.**
   - **Yếu tố pháp lý là một yếu tố quan trọng trong việc xác định giá trị của căn nhà, và các trạng thái pháp lý rõ ràng hơn thường có giá trị cao hơn.**
# Chạy thuật toán dự đoán giá
## Random Forest
![Chung cư](https://github.com/user-attachments/assets/f5160cbc-8d03-4171-9d3c-404bdac3630a)
- Out-of-Bag Score: 0.5576258770124625
- Mean Squared Error: 8958526101.841373
- Root Mean Squared Error: 94649.49076377206
- R-squared: 0.7459651275732477
## Gradient Boosting Machines
![Chung cư](https://github.com/user-attachments/assets/45b69bb7-ce05-4c8f-9047-54b76a8c4b74)
- Mean Squared Error: 7108940113.255908
- Root Mean Squared Error: 84314.53085474596
- R-squared: 0.7984134137434515


