FROM alpine:latest

RUN apk --no-cache add python3-dev
RUN apk add py3-pip 

WORKDIR /app

COPY . /app/

RUN pip --no-cache-dir install -r requirements.txt --break-system-packages

CMD [ "python3", "index.py" ]