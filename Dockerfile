FROM python:3.9.5

ADD . /SAP_project

WORKDIR /SAP_project

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]