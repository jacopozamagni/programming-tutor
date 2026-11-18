# \# Python Tutor

# 

# \[A simple programming tutor for students and people interessed in learning python.]

# 

# \## Screenshots

# !\[Explain tab](screenshots/explaination.png)

# !\[Generate exercise tab](screenshots/exercise.png)

# !\[Check code tab](screenshots/checkcode1.png)(screenshots/checkcode2.png)



# 

# \## Features

# \- \[Explain: what it gives the learner]

# \- \[Generate exercise: levels]

# \- \[Check code: hint, no solution]

# 

# \## How to run it

# 

# \*\*You need:\*\* Python 3.10 or newer, Git, and a free API key from \[Groq](https://console.groq.com).

# 

# 1\. Clone the repository and go into the folder:

# &#x20;  ```

# &#x20;  git clone https://github.com/jacopozamagni/programming-tutor.git

# &#x20;  cd programming-tutor

# &#x20;  ```

# 

# 2\. Create and activate a virtual environment (Windows):

# &#x20;  ```

# &#x20;  py -m venv .venv

# &#x20;  .venv\\Scripts\\activate.bat

# &#x20;  ```

# &#x20;  On macOS or Linux, use `python3 -m venv .venv` and `source .venv/bin/activate`.

# 

# 3\. Install the libraries:

# &#x20;  ```

# &#x20;  pip install -r requirements.txt

# &#x20;  ```

# 

# 4\. Set your Groq API key as an environment variable. In Windows:

# &#x20;  ```

# &#x20;  setx GROQ\_API\_KEY "your-key-here"

# &#x20;  ```

# &#x20;  Then close the terminal, open a new one, and activate the environment again. On macOS or Linux, use `export GROQ\_API\_KEY="your-key-here"`.

# 

# 5\. Start the app:

# &#x20;  ```

# &#x20;  streamlit run app.py

# &#x20;  ```

# &#x20;  It opens in your browser.

# 

# \*\*Note:\*\* the app uses the model `openai/gpt-oss-120b`. If you get a "model not found" or "blocked" error, open your Groq project's limits page and make sure that model is allowed, or change `MODEL` in `test\_api.py` to another chat model your account can use.

# \## How it works

# \[Two or three sentences: interface, your functions, Groq API, prompts kept separate.]

# 

# \## Limitations

# \- \[The tutor can be wrong. Mention the real wrong example you found.]

# \- \[It can't run your code.]

# \- \[Free tier rate limits.]

# 

# \## Future ideas

# \- \[Intra session memory, more programming languages supported ecc. ecc.]

