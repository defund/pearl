FROM python:3.6.3-slim

ADD pearl/ /pearl/
WORKDIR /pearl/

RUN pip install -r requirements.txt
RUN pip install --upgrade protobuf

CMD [ "python", "pearl.py" ]