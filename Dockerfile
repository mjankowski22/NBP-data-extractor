FROM python:3.9-slim-buster
RUN pip3 install --upgrade pip
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip3 --no-cache-dir install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]