FROM python:alpine3.7
WORKDIR /game
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3002
CMD [ "flask", "run", "--host=0.0.0.0", "--port=3002" ]