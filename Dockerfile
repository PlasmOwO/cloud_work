FROM python:3.9-slim
COPY . .
RUN pip install -r requirements.txt
RUN pip install fastapi[standard]
EXPOSE 8080
CMD ["python", "app.py"]
