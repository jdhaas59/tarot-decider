import pandas as pd
import random

# Define the tarot card deck
# Define the tarot card deck as a dictionary
tarot_deck = {
    "The Fool": "New beginnings, innocence, spontaneity",
    "The Magician": "Manifestation, resourcefulness, power",
    "The High Priestess": "Intuition, unconscious knowledge, mystery",
    "The Empress": "Fertility, femininity, beauty, nature",
    "The Emperor": "Authority, stability, leadership",
    "The Hierophant": "Tradition, conformity, morality",
    "The Lovers": "Love, harmony, relationships, values alignment",
    "The Chariot": "Control, willpower, success, action, determination",
    "Strength": "Inner strength, bravery, compassion",
    "The Hermit": "Contemplation, search for truth, inner guidance",
    "Wheel of Fortune": "Good luck, karma, life cycles, destiny, turning point",
    "Justice": "Justice, fairness, truth, cause and effect",
    "The Hanged Man": "Pause, surrender, letting go, new perspectives",
    "Death": "Endings, beginnings, change, transformation",
    "Temperance": "Balance, moderation, patience, purpose",
    "The Devil": "Materialism, bondage, ignorance, hopelessness",
    "The Tower": "Sudden change, upheaval, chaos, revelation",
    "The Star": "Hope, faith, renewal, inspiration, spirituality",
    "The Moon": "Illusion, fear, anxiety, subconscious",
    "The Sun": "Joy, success, vitality, life force",
    "Judgement": "Judgement, rebirth, inner calling, absolution",
    "The World": "Completion, integration, accomplishment",
    "Ace of Wands": "New beginnings, inspiration, invention",
    "Two of Wands": "Planning, decisions, leaving home, ambition",
    "Three of Wands": "Progress, expansion, exploration",
    "Four of Wands": "Celebration, harmony, marriage, home",
    "Five of Wands": "Strife, competition, challenge",
    "Six of Wands": "Victory, public recognition, progress",
    "Seven of Wands": "Challenge, competition, perseverance",
    "Eight of Wands": "Speed, action, air travel, movement",
    "Nine of Wands": "Endurance, perseverance, test of faith",
    "Ten of Wands": "Burden, responsibility, hard work",
    "Page of Wands": "Exploration, excitement, freedom",
    "Knight of Wands": "Energy, passion, adventure",
    "Queen of Wands": "Attractiveness, charisma, romance",
    "King of Wands": "Natural-born leader, vision, entrepreneur",
    "Ace of Cups": "Emotional fulfillment, joy",
    "Two of Cups": "Partnership, mutual support, attraction",
    "Three of Cups": "Abundance, fertility, beauty",
    "Four of Cups": "Loss, regret, disappointment",
    "Five of Cups": "Nostalgia, childhood memories, innocence",
    "Six of Cups": "Choices, variety, wishful thinking",
    "Seven of Cups": "Indecision, stuck in a rut, confusion",
    "Eight of Cups": "Emotional stability, contentment, satisfaction",
    "Nine of Cups": "Fantasy, illusion, overwhelmed by choices",
    "Ten of Cups": "Dreams, intuition, subconscious mind",
    "Page of Cups": "Mystery, fear, insecurity, illusion",
    "Knight of Cups": "Faith, spirituality, inner guidance",
    "Queen of Cups": "Harsh truth, painful realization",
    "King of Cups": "Mental clarity, truth, justice",
    "Ace of Swords": "Heartbreak, betrayal, severance",
    "Two of Swords": "Recovery, rest, contemplation",
    "Three of Swords": "Conflict, tension, deceit",
    "Four of Swords": "Trapped, powerless, self-imposed restriction",
    "Five of Swords": "Anxiety, fear, nightmares",
    "Six of Swords": "Endings, betrayal, loss, crisis",
    "Seven of Swords": "Guilt, self-punishment, subconscious release",
    "Eight of Swords": "Painful endings, betrayal, loss",
    "Nine of Swords": "New ideas, communication, mental clarity",
    "Ten of Swords": "Difficult choices, indecision, stalemate",
    "Page of Swords": "Heartbreak, rejection, emotional pain",
    "Knight of Swords": "Rest, retreat, contemplation",
    "Queen of Swords": "Loss, defeat, failure, betrayal",
    "King of Swords": "Moving on, leaving behind, moving away",
    "Ace of Pentacles": "Deception, trickery, dishonesty",
    "Two of Pentacles": "Isolation, self-imposed restriction, imprisonment",
    "Three of Pentacles": "Nightmares, anxiety, fear",
    "Four of Pentacles": "Depression, imprisonment, self-pity",
    "Five of Pentacles": "Recovery, change, transformation",
    "Six of Pentacles": "Ambition, conflict, rivalry, destruction",
    "Seven of Pentacles": "Hope, sudden change, upheaval, revelation",
    "Eight of Pentacles": "Faith, hope, renewal, spirituality",
    "Nine of Pentacles": "Optimism, success, vitality, achievement",
    "Ten of Pentacles": "Rebirth, inner calling, absolution",
    "Page of Pentacles": "Accomplishment, completion, fulfillment",
    "Knight of Pentacles": "New opportunities, inspiration, potential",
    "Queen of Pentacles": "Balance, adaptability, resourcefulness",
    "King of Pentacles": "Teamwork, collaboration, learning"
}

# Define the tarot card deck as a dictionary
tarot_deck = {
    "Card": list(tarot_deck.keys()),
    "Meaning": list(tarot_deck.values())
}

# Create DataFrame
tarot_df = pd.DataFrame(tarot_deck)

def draw():
    # Shuffle the DataFrame 7 times
    shuffled_tarot_df = tarot_df.copy()  # Make a copy of the original DataFrame

    for _ in range(7):
        shuffled_tarot_df = shuffled_tarot_df.sample(frac=1).reset_index(drop=True)

    random_number = random.randint(0, 77)
    return shuffled_tarot_df.iloc[random_number]