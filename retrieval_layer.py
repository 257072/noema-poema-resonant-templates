# retrieval_layer.py

import json
import os

# --- Poem Retrieval Index ---
poem_index = {}

def load_poem(title: str, filename: str):
    """Helper to load a tokenised poem JSON and add to poem_index."""
    path = os.path.join("curated_poems", filename)
    with open(path, "r", encoding="utf-8") as f:
        poem_index[title] = json.load(f)

# --- Load Poems ---

load_poem("6 - Angels on Earth", "06_Angels_on_Earth_tokenised.json")
load_poem("Forgiveness", "08_Forgiveness_tokenised.json")
load_poem("Love Is", "09_Love_Is_tokenised.json")
load_poem("Holiness Of The Heart", "54_Holiness_Of_The_Heart_tokenised.json")
load_poem("Elixir Of Love", "55_Elixir_Of_Love_tokenised.json")
load_poem("The Second Coming", "59_The_Second_Coming_tokenised.json")
load_poem("Golden Nuggets", "66_Golden_Nuggets_tokenised.json")
load_poem("Inversion", "68_Inversion_tokenised.json")
load_poem("The True Role Of The Ego", "72_The_True_Role_Of_The_Ego_tokenised.json")
load_poem("Creatrix", "73_Creatrix_tokenised.json")
load_poem("Faith", "82_Faith_tokenised.json")
load_poem("Liberty Moon", "91_Liberty_Moon_tokenised.json")
load_poem("Do What The Robot Says", "93_Do_What_The_Robot_Says_tokenised.json")
load_poem("Heart Supported Mind", "96_Heart_Supported_Mind_tokenised.json")
load_poem("Human Amnesia", "97_Human_Amnesia_tokenised.json")
load_poem("Kaleidoscope Memories", "99_Kaleidoscope_Memories_tokenised.json")
load_poem("Calibrate (A PoêManifesto)", "100_Calibrate_tokenised.json")

# --- Retrieval Function ---

def get_poem(title: str):
    """Fetch poem tokens by title."""
    return poem_index.get(title)

# --- Example Usage ---
if __name__ == "__main__":
    poem_data = get_poem("Calibrate (A PoêManifesto)")
    print(json.dumps(poem_data, indent=2, ensure_ascii=False))
