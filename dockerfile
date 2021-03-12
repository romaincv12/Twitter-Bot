FROM python:3.7-alpine

COPY config.py /bots/
COPY stream_bot.py /bots/
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "stream_bot.py"]