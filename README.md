# take_home

## Completed Tasks

I was able to develop some of this application, for example I was able to get a webserver up and able to respond to a GET request. The database is running and a shell script is able to create a database and a table.

## Tasks Not Complete

I was not able to get the server to connect to the database. The last error I received was 
involved the library libpq-fe.h.

In retrospect I would have been more successful in the project if:

- I knew the commands `docker stop [image]`,`docker system prune` and `docker system prune -a`, manually deleting files above the root directory was not a good idea. This mistake set me back a day.

- I had a better understanding of where Docker images are created and how they can communicate 
 
- I had found the correct image to use in the Dockerfile. Also, when I started the project I read that having more than one FROM in the Dockerfile changes the way it builds. That is why I attempted to start with one `FROM library/postgres`, as to not add more complexity to the build.


