FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install ruff pytest
