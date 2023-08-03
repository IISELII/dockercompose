# python base image in the container from Docker Hub
FROM python:3.8.12-buster

# copy files to the /app folder in the container
COPY fast.py /app/fast.py
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
COPY Model.py /app/Model.py
COPY iris_model.joblib /app/iris_model.joblib
COPY iris.csv /app/iris.csv

# set the working directory in the container to be /app
WORKDIR /app


# install the packages from the Pipfile in the container
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# expose port for the Streamlit web server
EXPOSE 8000

# execute the command python main.py (in the WORKDIR) to start the app
CMD uvicorn fast:app --host 0.0.0.0 --port 8000
