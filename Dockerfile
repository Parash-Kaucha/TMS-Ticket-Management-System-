FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /tms
COPY requirements.txt /tms/
RUN pip install update
RUN pip install -r requirements.txt
COPY . /tms/