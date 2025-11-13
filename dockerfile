FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY chatbot.py .

EXPOSE 8501

CMD ["streamlit","run","chatbot.py"]