FROM python:3.9-slim
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "app:app","--port","80"]
