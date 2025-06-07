# LangchainProject

## Cách setup:
B1: Lấy API Key từ Google AI Studio, thay thế api-key trong file .env trong folder backend
B2(optional): Lấy API Key từ OpenAI, cần phải liên kết thẻ credit card mới dùng được
B3: Tải các thư viện python cần thiết có trong file requirements.txt, có thể kiểm tra và tải toàn bộ bằng lệnh pip install -r backend/requirements.txt (yêu cầu python 3.10 trở lên)
B4: Tải WAMP server cho Windows (MAMP cho MacOS) và set up PhpAdmin. Tạo CSDL langchain (có thể dùng tên khác nhưng cần chỉnh lại trong product_info.py). Import file products.sql để import table products. Điều chỉnh password trong file product_info.py trong thư mục backend\utility cho giống với máy đang chạy (đổi password tài khoản admin trong phpAdmin)

## Cách chạy:
B1: Chạy backend: Tới đường dẫn backend bằng lệnh cd backend, chạy backend bằng lệnh python app.py  
B2: Chạy Frontend: index.html
*Trong file .env chọn AI provider, mặc định là Google AI Studio
B3: Nhấn Ctrl + C trong console chạy backend để dừng

## chạy backend_old:
Không cần WAMP server hay mysql. Chỉ cần có API Key từ Google AI Studio. Lấy dữ liệu từ file products.json
Các bước chạy cũng giống như trên, backend chạy appJson.py trong backend_old, frontend chạy index.html

