FROM python:3

COPY . .

RUN pip install -r requirments.txt
RUN cd voting
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]