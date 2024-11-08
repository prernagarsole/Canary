FROM python:3.9-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/app.py .
ENV VERSION=v2
ENV APP_COLOR=green
EXPOSE 5000
CMD ["python", "app.py"]
