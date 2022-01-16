FROM python:3.9-slim-buster

WORKDIR /app

COPY ["./app/app.py", "./app/dna_image.jpg", "/app/"]

RUN mv /app/app.py /app/dna_count.py \
    && pip3 install --no-cache-dir streamlit pandas

CMD streamlit run dna_count.py

EXPOSE 8501