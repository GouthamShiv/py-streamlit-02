FROM python:3.9-slim-buster

WORKDIR /app

COPY ["./app/app.py", "./app/dna_image.jpg", "requirements.txt", "/app/"]

RUN mv /app/app.py /app/dna_count.py \
    && pip3 install --no-cache-dir -r requirements.txt

CMD streamlit run dna_count.py --server.enableCORS=false --server.enableXsrfProtection=false

EXPOSE 8501