FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Now install requirements
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
