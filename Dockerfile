FROM python:3.14-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Grant execution permissions to the script inside the working directory
RUN chmod +x ./start.sh

EXPOSE 8000 8501

CMD ["./start.sh"]