FROM python:3.7

COPY ./app /app
COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
RUN chmod u+x /app/main.py

CMD python3 app/timer.py
