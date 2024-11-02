FROM docker.fxxk.dedyn.io/alpine
LABEL maintainer="1415584788@qq.com"
RUN apk add --update nodejs nodejs-npm

COPY . /src
WORKDIR /src

RUN npm install
EXPOSE 8080