# retrieval_layer.py

import json

# Load tokenised poem
with open('6_Angels_on_Earth_tokenised.json', 'r', encoding='utf-8') as f:
    angels_on_earth_tokens = json.load(f)

# Retrieval index
poem_index = {
    "6 - Angels on Earth": {
        "filename": "6_Angels_on_Earth_tokenised.json",
        "year": 1995,
        "tokens": angels_on_earth_tokens
    }
}

# Example function to fetch a poem by title
def get_poem(title):
    return poem_index.get(title, None)

# Example usage
if __name__ == "__main__":
    poem_data = get_poem("6 - Angels on Earth")
    print(poem_data)

import json

# Load Forgiveness poem tokens
with open('curated_poems/08_Forgiveness_tokenised.json', 'r', encoding='utf-8') as f:
    forgiveness_tokens = json.load(f)

# Add to the retrieval index
poem_index["Forgiveness"] = forgiveness_tokens

# Load Love Is
with open('curated_poems/09_Love_Is_tokenised.json', 'r', encoding='utf-8') as f:
    love_is_tokens = json.load(f)
poem_index["Love Is"] = love_is_tokens

# Load Holiness Of The Heart
with open('curated_poems/54_Holiness_Of_The_Heart_tokenised.json', 'r', encoding='utf-8') as f:
    holiness_tokens = json.load(f)
poem_index["Holiness Of The Heart"] = holiness_tokens

# Load Elixir Of Love
with open('curated_poems/55_Elixir_Of_Love_tokenised.json', 'r', encoding='utf-8') as f:
    elixir_tokens = json.load(f)
poem_index["Elixir Of Love"] = elixir_tokens

# Load The Second Coming
with open('curated_poems/59_The_Second_Coming_tokenised.json', 'r', encoding='utf-8') as f:
    second_coming_tokens = json.load(f)
poem_index["The Second Coming"] = second_coming_tokens

# Load Golden Nuggets
with open('curated_poems/66_Golden_Nuggets_tokenised.json', 'r', encoding='utf-8') as f:
    golden_nuggets_tokens = json.load(f)
poem_index["Golden Nuggets"] = golden_nuggets_tokens
