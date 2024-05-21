FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y ffmpeg
RUN apt install git -y
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "python", "-u", "main.py" ]
