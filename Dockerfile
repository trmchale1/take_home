FROM library/postgres

# set environmental variable to build argument mode
ARG mode
ENV MODE=$mode

WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y lsb-release && apt-get clean all
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install curl
RUN apt-get -y install wget
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3-pip
RUN apt-get update
RUN apt-get -y upgrade
RUN pip3 install -r requirements.txt
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install postgresql
RUN apt-get update
RUN apt-get -y upgrade

RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh

ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# container by default runs sleep infinity when started
CMD ["sleep", "infinity"]
