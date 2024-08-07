# what is this project?

it _should be_ a E-Commerce Website made with django library in python language
it's my first time making it so it won't be as good as the known websites

no one ask me about the Front-end cuz it's all made by ChatGPT i only did some changes to the templates _i only know Back-end and some HTML_

## how to install it

- no need to mention that python should be installed on your machine :)

- do you see the file called "setup_env.bat"? _(works on windows)_

- just run it and it will create a virtual environment and activate it

- also it will download the requirements that is written in the file called "requirements.txt" _actually it just contain django_

- you need to do something important which is creating a super user to access the admin site:
  in the terminal type "python manage.py createsuperuser" and it will ask you to input some credentials and then you're done
  _(the admin site allows you to control everything in the website.. just like adding, removing or updating products and more)_

_maybe you got bored but we're about to finish :D_

- one important step is to make migrations _it's like sending the data to the database_
  to do so you need to type in the terminal: "python manage.py makemigrations",
  and then type "python manage.py migrate"

_if you face any error google it :)_

- so after doing all these things you have to run the server to make the Website up and running

- to do so, just type in the terminal "python manage.py runserver" and it will show you a line says: "Starting development server at.." after this you will find the link

## my progress until the moment i'm writing this:

well...
just discover by yourself :)

that's it for now if i remember something i will write it
