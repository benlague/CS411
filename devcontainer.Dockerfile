FROM nikolaik/python-nodejs:python3.6-nodejs14

RUN apt-get update && apt-get install -y curl wget vim build-essential \
    git file sudo libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev sqlite3 nano postgresql postgresql-contrib 

RUN pip install --upgrade pip

RUN npm install -g @vue/cli

RUN wget http://download.redis.io/redis-stable.tar.gz && \
    tar xvzf redis-stable.tar.gz && \
    cd redis-stable && \
    make && \
    make install

RUN apt-get install libpq-dev