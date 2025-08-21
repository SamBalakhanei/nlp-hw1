Prerequisites: Python, Git
Python download: https://www.python.org/downloads/
Git download: https://git-scm.com/downloads


0. Open terminal and run the command "git clone https://github.com/SamBalakhanei/nlp-hw1.git"
1. Run the command "cd nlp-hw1"
2. Create a python virtual environment by running the command "python -m venv venv"
3. Activate the virtual environment by running the command "source venv/bin/activate" (UNIX) or "call venv/Scripts/activate" (Windows CMD)
4. Run the command "pip install -r requirements.txt"
5. Go to https://huggingface.co/settings/tokens and click "Create New Token" at the top right
6. Select "Read", give your token a name, and click "Create Token"
7. Copy the token
8. Create a file in nlp-hw1 called ".env" (/nlp-hw1/.env)
9. In this file, write "HF_TOKEN=<your_token_here>" and replace "<your_token_here>" with the token copied in step 7
10. Save the .env file
11. Run the command "python main.py"

Output should look something like this:

1. Where has all the money in the world gone?

Honest question.

Where is all the money?  I hear nothing but bad news about financial crisis all over the world, an...
Sentiment: Neutral.

2. Is there a better sub where comments aren’t hidden 99.9% of the time?

So often someone will ask an amazing question, something I’m really interested in getting...
Sentiment: Negative.

3. How real-world corruption works.

This is a throwaway account (I'm a longtime redditor under another login). /r/economics might not be the correct place to put ...
Sentiment: Negative.

4. CLASS ACTION AGAINST ROBINHOOD. Allowing people to only sell is the definition of market manipulation. A class action must be started, Robinhood has made plenty...
Sentiment: Negative.

5. Wallstreet Bets Set to Private Megathread

The moderators there have made that sub private before. That’s why this sub was created. It’ll probably open back up ...
Sentiment: Neutral.