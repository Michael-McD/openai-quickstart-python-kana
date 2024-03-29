# OpenAI API Kanji to Kana - Python example app

This is a Japanese Kanji to Kana generator app based on the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python-kana
   ```

4. Create a new virtual environment (I've used [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) to do this.):

   ```bash
   $ conda create --name quickstart-kana python=3.11.5 openai flask
   $ conda activate quickstart-kana
   ```

5. Install the requirements:

   ```bash
   $ conda env create -f environment.yaml
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file. I have used an environment variable `$OPENAI_API_KEY`.

8. Run the app:
`
   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind the original example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
