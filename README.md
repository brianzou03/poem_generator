# Acrostic Poem Generator [Creative Writing]
I created the acrostic poem generator that takes in a poem (or any collection of sentences of your choice)
and generates a poem by taking the first character of each of the words in the original text
and providing a new word for each of the characters using one of the 10,000 most common english words.
The purpose of this application is to provide inspiration for poetry writing. The generated texts are very
abstract in nature and require some interpretation to appreciate. This serves as a good exercise to practice 
poetry writing, poetry generation, and interpreting works of poetry in your own way.

#### Steps to run app

1. Enter the virtual environment setup in your command line (commands shown below)
2. In command line, run ```pip install -r requirements.txt```
3. Run [script.py](script.py) to fetch the 10,000 most common english words
4. Go to [main.py](main.py) and alter the array to fit your original poem or sentences
5. Run [main.py](main.py)
6. The poem is produced in console output. Enjoy!

#### Virtual Environment Setup
```commandline
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
```

#### Most common 10,000 words
The most common 10,000 words are available in the following repo, thanks to GitHub user worldlywisdom.
https://github.com/first20hours/google-10000-english