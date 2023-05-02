FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install ruff pytest

COPY 8001175981_pa4.py ./
COPY CSVHelper.py ./
COPY DirectoryMgr.py ./
COPY InputMgr.py ./
COPY Joiner.py ./
COPY ModifyCSV.py ./
