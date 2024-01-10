FROM python:slim
COPY . /root 

RUN chmod +x /root/gen_flag
RUN chmod +x /root/cryptic_algo.py
RUN chmod +x /root/p01.py
RUN chmod +x /root/p02.py

WORKDIR /app
EXPOSE 8080
CMD ["python", "-m", "http.server", "8080"]
