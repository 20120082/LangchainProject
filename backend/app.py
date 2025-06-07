from flask import Flask, request, jsonify, session
import json
import os
from dotenv import load_dotenv
from flask_cors import CORS
from config import AI_PROVIDER
from utility.product_info import get_product_info

# Load API key
load_dotenv()

# chọn AI provider
if AI_PROVIDER == 'google':
    from ai_providers.google_ai import build_conversation_chain
else:
    from ai_providers.openai import build_conversation_chain

# Khởi tạo conversation
conversation, chain_memory = build_conversation_chain()

# Hàm reset lại memory mỗi khi chạy lại
def reset_memory():
    print("Reset memory khi khởi động lại")
    chain_memory.chat_memory.clear()

# Flask setup
app = Flask(__name__)
reset_memory()
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your-secret") # Secret key này thực tế set trong .env, mỗi lần chạy cần tạo key ngẫu nhiên
CORS(app)

#define route cho app
@app.route('/api/chat', methods=['POST'])

def chat():
    # Nhận message từ người dùng
    user_message = request.json.get('message')

    # Khởi tạo history từ chain_memory
    history = chain_memory.chat_memory.messages
    # Kiểm tra nội dung memory trên console
    print("Hiện tại memory gồm:")
    for m in history:
        print(f"- {m.type}: {m.content}")
    # Kiểm tra memory có rỗng không
    is_first = len(history) == 0
    
    if is_first:
        context = f"""
        Bạn là một người bán hàng đồ dùng học tập thân thiện và nhiệt tình. Dưới đây là thông tin sản phẩm mà bạn có thể dùng để tư vấn:

        {get_product_info()}

        Trả lời ngắn gọn, thân thiện. Nếu khách hàng thêm sản phẩm mới, bạn nhớ lưu vào trí nhớ để lần sau có thể tính tổng toàn bộ.
        """
        # Thêm vào chain các thông tin cần khởi tạo
        chain_memory.chat_memory.add_user_message("__init__")

        # Tách từng dòng trong context và lưu từng dòng vào memory để dễ đọc
        for line in context.strip().split('\n'):
            if line.strip():
                chain_memory.chat_memory.add_ai_message(line.strip())
        print("Đã khởi tạo dữ liệu sản phẩm trong memory.")

    # Gửi câu hỏi thật sự
    response = conversation.run(input=user_message)
    # filter lại history để hiện thị message phù hợp
    history = chain_memory.load_memory_variables({})['history']
    filtered_history = [
        msg.content for msg in history
        if msg.content.strip() != "__init__"
    ]

    return jsonify({
        'response': response,
        'history': filtered_history,
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)