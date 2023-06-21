FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir database

COPY . .

CMD ["python", "scripts/run_setup.py"]
CMD ["python", "scripts/run_load_data.py"]
CMD ["python", "scripts/gui_main.py"]