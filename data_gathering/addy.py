npc = "https://stardewvalleywiki.com/Villagers"
npc_pages = ['/Alex','/Elliott','/Harvey','/Sam','/Sebastian','/Shane','/Abigail','/Emily','/Haley','/Leah',
             '/Maru', '/Penny','/Caroline', '/Clint', '/Demetrius', '/Dwarf', '/Evelyn', '/George', '/Gus',
             '/Jas', '/Jodi', '/Kent', '/Krobus', '/Leo', '/Lewis', '/Linus', '/Marnie', '/Pam', '/Pierre',
             '/Robin', '/Sandy', '/Vincent', '/Willy', '/Wizard', '/Birdie', '/Bouncer', '/Fizz', '/Gil',
              '/Governor', '/Grandpa', '/Gunther', '/Henchman', '/Marlon', '/Morris', '/Mr._Qi', '/Professor_Snail']

# Goal: Build a dataset of characters, how they say it, when they say it, and the face they make
# 1: Scrape the description of each NPC
# 2: Scrape the text of each NPC's heart events
# 3: Build a json dataset
# 4: Label the dataset, and fine-tune a model to generate text in the style of each NPC
# - Labels: Name, Context, Face
# + Context: Emotion, Time of day, Location
# + Face: Each character has a set of faces, with naming scheme scrapable from the wiki

# Approach:
# 1:
'''
Fine-tune a model on the way each NPC speak, and create a chat interface where
the user can talk further with the NPC. 
The model should be able to analyze the user's input, form a response based on
the knowledge and style of the NPC, and generate a face to go with it.
'''
# 2:
'''
Intercept the game's dialogue system, and replace the text with the model's output.
This should be easier, but less fun than the first approach.

'''
# Model choice:
# Currently trying llama3.2:3b but might switch to a lighter model, depending on the performance
# 
# Further goals:
'''
- Scrape the schedule, likes and dislikes
- 
'''