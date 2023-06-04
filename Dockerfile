FROM python:3.8

WORKDIR /
COPY . .

RUN pip install -r requirements.txt

RUN export FLASK_DEBUG=1

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
