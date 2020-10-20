# our base image
FROM tiangolo/uvicorn-gunicorn:python3.7

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY ./app /app

# tell the port number the container should expose
EXPOSE 80


# run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
