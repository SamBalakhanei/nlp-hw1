import os
from typing import Optional
from datasets import load_dataset
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
DATASET_ID = "winddude/reddit_finance_43_250k"
SPLIT = "train"
SUBSET = 5
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise Exception("No HF_TOKEN found. Refer to steps 5-10 in the README.md")

client = InferenceClient(model=MODEL, token=HF_TOKEN)

SYSTEM_PROMPT = (
    "You are a finance NLP assistant.\n"
    "Classify the sentiment of the given Reddit finance text as exactly one of:\n"
    "Positive, Neutral, or Negative.\n"
    "Respond with one word only. No explanation."
)

def find_text(row: dict) -> Optional[str]:
    '''Get title and body'''
    title = row.get("title")
    body = row.get("selftext")
    return f"{title}\n\n{body}"

def classify(text: str) -> str:
    user_prompt = f"Text:\n{text}\n\nLabel:"
    res = client.chat.completions.create(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=8,
    )
    return res.choices[0].message.content.strip()

def main():
    ds = load_dataset(DATASET_ID, split=SPLIT)
    shown = 0
    for row in ds:
        text = find_text(row)
        if not text:
            continue
        sentiment = classify(text)
        shown += 1
        print(f"{shown}. {text[:160].replace('\\n',' ')}{'...' if len(text) > 160 else ''}")
        print(f"Sentiment: {sentiment.split(' ')[0]}\n")
        if shown >= SUBSET:
            break

main()