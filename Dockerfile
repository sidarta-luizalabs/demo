FROM python
WORKDIR /usr/src/app
COPY app.py ./
RUN pip install flask
CMD [ "python", "./app.py" ]
