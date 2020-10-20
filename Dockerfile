# our base image
#FROM tiangolo/uvicorn-gunicorn:python3.7
FROM python:3.7

## make a local directory
RUN mkdir /bbl_api_data
ENV PATH=$PATH:/bbl_api_data
ENV PYTHONPATH /bbl_api_data

# install Python modules needed by the Python app
COPY requirements.txt /bbl_api_data/
RUN pip install --no-cache-dir -r /bbl_api_data/requirements.txt


# copy files required for the app to run
COPY ./app /bbl_api_data/app


WORKDIR /bbl_api_data

# tell the port number the container should expose
EXPOSE 80

# run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
