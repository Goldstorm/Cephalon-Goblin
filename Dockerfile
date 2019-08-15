FROM python:3.6
MAINTAINER Nick Goldstein <nick@nickgoldstein.com>
COPY requirements.txt .
COPY components/token.json components/
RUN pip install -r requirements.txt
COPY . /opt/goblin
CMD ["python3", "/opt/goblin/bot.py"]