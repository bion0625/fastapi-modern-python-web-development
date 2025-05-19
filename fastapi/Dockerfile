FROM python:3.13.3
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/app
ENV PYTHONPATH=/code/app
# CMD ["python", "/code/app/main.py"]
CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
# docker image build -t bion0625/fastapi-test-project:v1 .
# docker run -p 8000:8000 bion0625/fastapi-test-project:v1