FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install ruff pytest

COPY 8001175981_pa4.py ./

CMD ["python", "./8001175981_pa4.py"]
