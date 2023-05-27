# OpenAI Ticket Analysis - Python example app with Flask

This is an example web app based on the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart) can be used to assist with qaulity assurance of tickets by analyising the content and producing sentiment results. The app uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. 

Follow the instructions below to get set up.

The app once loaded, should look like the following: 

<img width="1156" alt="Screenshot 2023-05-27 at 16 55 30" src="https://github.com/dooley1001/openai-ticketAnalysis-python/assets/30215810/6f167c48-6958-4377-bdfd-2682e6e79d82">


## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
# openai-ticketAnalysis-python
