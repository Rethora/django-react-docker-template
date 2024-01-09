FROM nikolaik/python-nodejs:python3.10-nodejs20-slim-canary

WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
