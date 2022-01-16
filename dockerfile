FROM python:3.9-slim-buster

WORKDIR /app

COPY /app/app.py /app/DNAcount.py

RUN pip3 install streamlit pandas

CMD streamlit run DNAcount.py

EXPOSE 8501