# set base image
FROM python:3.8

# set the working directory in the container
WORKDIR /okay_stone

# github
RUN git clone https://github.com/jonathanmagliano/api-razao-cliente.git

# copy the content of the awesome project to the working directory
COPY hello_stone/ .

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "./manage.py", "runserver" ]
