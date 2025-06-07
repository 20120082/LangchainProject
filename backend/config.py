import os
from dotenv import load_dotenv

load_dotenv()

# Chọn 'openai' hoặc 'google'
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")
