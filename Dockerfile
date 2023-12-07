FROM ubuntu

WORKDIR /app

COPY requirement.txt /app
COPY django_study_buddy /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt && \
    cd django_study_buddy 

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8080"]
