FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENV FLASK_APP=project_module/views.py

CMD ["flask", "run", "--host", "0.0.0.0", "-p", "5000"]

# CMD flask --app project_module/views.py run --port 5000

# CMD flask --app project_module/views.py run --host 0.0.0.0 --port 5000:5000