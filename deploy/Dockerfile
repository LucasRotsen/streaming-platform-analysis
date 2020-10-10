FROM python:3.8.1

WORKDIR /streaming-platform-analysis/

COPY requirements.txt /streaming-platform-analysis/

RUN pip install -r requirements.txt

COPY src /streaming-platform-analysis/src
COPY data /streaming-platform-analysis/data

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py"]