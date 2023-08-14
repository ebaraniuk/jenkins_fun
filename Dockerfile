FROM python:3.11
WORKDIR .
ADD main.py .
ADD tests.py .
CMD ["python", "tests.py"]

