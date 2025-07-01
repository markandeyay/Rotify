import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(text):
    prompt = (
        "in text that takes no longer than 30 seconds to read outloud, take the following web page content and explain it with an unhinged gen-z tiktok-style brainrot summary. "
        "don’t be professional. be borderline incomprehensible but still funny. think subway surfers background energy. "
        "speak in all lowercase and no punctuation. use emojis like 😭 💔 🥀 🙏 — but not all at once. "
        "don’t say the word brainrot. "
        "ok start using words like icl ts pmo sm n so rn ngl r u srsly srs n fr rn vro lol atp js go b fr vro idek nm brb gng gtg atm bt ts pyo 2 js lmk lol onb fr nty b fr rn lk br. "
        "avoid words like 'vibin', 'gang', 'no cap', 'bestie', 'grindset', 'thicc', or 'thingy'. "
        "make sure it's still understandable to a brainrot-literate audience, under 1000 words ideally, but include key info like numbers or stats from the original.\n\n"
        f"webpage content:\n{text}"
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "you're a sarcastic gen-z content creator"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.95,
    )

    return response.choices[0].message.content
