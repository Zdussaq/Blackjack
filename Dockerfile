FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# run the command
ENTRYPOINT [ "python", "sources/Dealer.py" ]