FROM python:3.9-slim
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "app:app","--port","8080"]
