# python base image in the container from Docker Hub
FROM python:3.8.12-buster

# copy files to the /app folder in the container
COPY streamlit.py /app/streamlit.py
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

# set the working directory in the container to be /app
WORKDIR /app

# install the packages from the Pipfile in the container
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# expose port for the Streamlit web server
EXPOSE 8501

# execute the command to start Streamlit app
CMD streamlit run streamlit.py --server.port 8501
