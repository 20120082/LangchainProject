import pymysql
import json

def fetch_products_from_mysql():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='langchain',
        charset='utf8mb4'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

def get_product_info():
    """Convert product data to text for the AI"""
    products = fetch_products_from_mysql()
    product_lines = []
    for product in products:
        feature = ', '.join(json.loads(product['feature']))
        line = f"- {product['name']} ({product['category']}) – {product['price']:,} VND. {product['description']}. Tính năng: {feature}"
        product_lines.append(line)
    return "\n".join(product_lines)
