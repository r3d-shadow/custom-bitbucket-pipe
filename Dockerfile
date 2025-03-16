FROM python:3.10-slim
ENV WORKDIR /PIPE
WORKDIR $WORKDIR

COPY pipe ./
RUN pip install --no-cache-dir -r ./requirements.txt
COPY LICENSE.txt README.md pipe.yml ./

ENTRYPOINT ["python3", "/PIPE/main.py"]