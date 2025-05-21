# LangchainProject

## Cách sử dụng:
B1:Lấy API Key từ Google AI Studio, thay thế api-key trong file .env trong folder backend  
B2:Tải các thư viện python cần thiết có trong file requirements.txt bằng lệnh pip install -r backend/requirements.txt (yêu cầu python 3.10 trở lên)  
B3:Chạy backend: Tới đường dẫn backend bằng lệnh cd backend, chạy backend bằng lệnh python app.py  
B4:Chạy Frontend: index.html

## Update note:
1.Chuyển sang dùng cơ sở dữ liệu mySQL thay vì file json. mySQL cài từ WAMP và quản lý bởi phpAdmin.
    -> Cài đặt cơ sở dữ liệu trên phpAdmin. Chỉ cần tạo CSDL: langchain 
        -> Còn table products thì import file products.sql trong thư mục sql

2.Trong app.py phần def fetch_products_from_mysql() -> kiểm tra user, password và database, mỗi máy có thể khác nhau

3.cần cài thêm 2 thư viện bằng lệnh pip install
    pymysql
    cryptography

