from flask import Flask, request, jsonify
from langchain_google_genai import GoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import json
import os
from dotenv import load_dotenv
from flask_cors import CORS


# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

app = Flask(__name__)
CORS(app)

# Load product from json
with open('products.json', 'r', encoding='utf-8') as f:
    products_data = json.load(f)

# Initialize Gemini model
llm = GoogleGenerativeAI(model="gemini-2.0-flash",google_api_key=api_key, temperature=0.7)

# Create conversation memory
memory = ConversationBufferMemory()

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def get_product_info():
    """Convert product data to text for the AI"""
    product_text = "Thông tin sản phẩm:\n"
    for product in products_data['products']:
        product_text += f"""
        - Tên: {product['name']}
          Danh mục: {product['category']}
          Giá: {product['price']:,} VND
          Mô tả: {product['description']}
          Tính năng: {', '.join(product['features'])}
        """
    return product_text

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Get product info
    product_info = get_product_info()
    
    # Create prompt 
    prompt = f"""
    Bạn là một người bán hàng đồ dùng học tập thân thiện và nhiệt tình. 
    Hãy trả lời câu hỏi của khách hàng dựa trên thông tin sản phẩm dưới đây.
    
    {product_info}
    
    Lịch sử trò chuyện:
    {memory.load_memory_variables({})['history']}
    
    Câu hỏi của khách hàng: {user_message}
    
    Câu trả lời:
    """
    
    # Get AI response
    response = conversation.predict(input=prompt)
    
    return jsonify({
        'response': response,
        'history': memory.load_memory_variables({})['history']
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)