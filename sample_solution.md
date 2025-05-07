This will give you instructions on how to run the sample solution.

## Ollama

If you did not work on your private machine during the course, you need to install ollama first. Follow the instructions in `01_ollama.md` until step 2.

## Cloning the repositories to your machine

Recommendation: Create a new folder, called IDW. Open a CMD in this folder and execute the following two commands:

`git clone https://github.com/c-giese/idw-backend.git`
`git clone https://github.com/c-giese/idw-frontend.git`

Now you have the two repos on your machine.

## Backend

Before we start the backend, wie need to create a virtual environment. Navigate to the base directory of the backend (if you still have the terminal open from cloning, simply type cd idw-backend).
There follow the instructions in `02_virtual_environment.md`. Install all the dependencies with `pip install -r .\requirements.txt`.
Now you can start the backend. Type `py .\code_examples\07_flask_chatbot.py` in the terminal, where you have just installed the .venv.

## Frontend

For this step there are two requirements:

1. Install node.js (https://nodejs.org/en) simply download and execute it
2. Install the angular-cli (https://angular.dev/tools/cli/setup-local#install-the-angular-cli) after you installed node.js, you can open a terminal anywhere and run `npm install -g @angular/cli`. This enables you to use angular.

Go to the directory of the frontend. If you followed my recommendation, you can find it here: .../IDW/idw-frontend. Open a terminal there and run `npm install`. This will install all dependencies.
After the process succeeded, you can type in the same terminal `ng serve` this starts the frontend. It will open at localhost:4200, you can type this in your browser to view the website. UNder the "Chat"-tab you find the sample solution and can play around with it.


If you encounter any error or problem, don't hesitate to gwt in contact with me :)