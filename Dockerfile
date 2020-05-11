FROM python:3

RUN pip install pyzmq locustio faker names faker

ADD locustfile.py /config/locustfile.py
ADD runLocust.sh /usr/local/bin/runLocust.sh

RUN ["chmod", "+x", "/usr/local/bin/runLocust.sh"]

ENV LOCUST_FILE /config/locustfile.py

EXPOSE 8090

ENTRYPOINT ["/usr/local/bin/runLocust.sh"]