# Pull official base image
FROM python:3.9.2-slim-buster

# Set working directory
ARG WORKDIR=/usr/src/app
WORKDIR ${WORKDIR}

# Set environment variables FOR PYTHON EXECUTION
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x ${WORKDIR}/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]