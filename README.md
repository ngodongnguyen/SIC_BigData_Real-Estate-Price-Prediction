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
    <img src="[https://github.com/user-attachments/assets/afd5f2f3-71e0-4780-901a-f4967f569d7e](https://github.com/user-attachments/assets/f850a58d-ec11-4adb-b038-5e9594ab3cba)" alt="Dữ liệu về nhà ở">
</div>
  <div style="text-align: center;">
    <strong>Đất</strong><br>
    <img src="[https://github.com/user-attachments/assets/afd5f2f3-71e0-4780-901a-f4967f569d7e](https://github.com/user-attachments/assets/6f613e30-02dd-42ba-b476-16e149ba02f7)" alt="Dữ liệu về đất">
</div>



    - Vấn đề: Ở đây dữ liệu thiếu khá nhiều, và sẽ có một số cột không ảnh hưởng đến output giá chung cư nên sẽ phải tiền xử lý, trực quan hoá các cột dữ liệu để tìm ra dữ liệu nào được giữ lại để xây dựng cho quá trình traning ***(tiền xử lý sẽ được trình bày bên dưới)***




