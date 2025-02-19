from deliverable2 import *  
import json

# Instantiate the URLValidator class
validator = URLValidator()

# Define the dataset manually as a list of dictionaries
data = [
    {"user_prompt": "I just finished watching a horror movie alone at night.", 
     "url_to_check": "https://www.quora.com/How-does-it-feel-watching-a-horror-film-alone-at-night"},

    {"user_prompt": "My cat keeps staring at the wall like it sees a ghost.", 
     "url_to_check": "https://cats.com/why-is-my-cat-staring-at-the-wall#:~:text=Feline%20hyperesthesia%20syndrome%20consists%20of,suffering%20from%20feline%20hyperesthesia%20syndrome."},

    {"user_prompt": "I accidentally sent an email to the wrong person at work.", 
     "url_to_check": "https://www.quora.com/What-should-you-do-if-you-accidentally-send-an-email-to-the-wrong-person-Is-it-possible-to-retrieve-the-email-or-should-you-contact-the-recipient-and-ask-them-not-to-open-it#:~:text=1%3E%20Quickly%20Acknowledge%20Your%20Mistake,meant%20for%20you”%20can%20suffice."},

    {"user_prompt": "My internet went out in the middle of an important online meeting.", 
     "url_to_check": "https://www.remotestaff.ph/blog/help-what-should-i-do-when-internet-goes-out-while-im-at-meeting/#:~:text=Contact%20your%20Boss%20or%20Client,disappearance%20during%20the%20online%20meeting."},

    {"user_prompt": "I found an old childhood toy, and now I feel nostalgic.", 
     "url_to_check": "https://www.letmeorganizeit.com/the-power-of-nostalgia"},

    {"user_prompt": "I tried to bake a cake, but it turned out like a rock.", 
     "url_to_check": "https://cooking.stackexchange.com/questions/92863/why-does-my-cake-get-hard-after-baking"},

    {"user_prompt": "I got lost in my own neighborhood while taking a walk.", 
     "url_to_check": "https://www.myptsd.com/threads/got-lost-in-my-own-neighborhood-this-morning-again.21073/"},

    {"user_prompt": "My phone’s autocorrect just embarrassed me in a group chat.", 
     "url_to_check": "https://discussions.apple.com/thread/255139446?sortBy=rank"},

    {"user_prompt": "I accidentally spilled coffee on my laptop.", 
     "url_to_check": "https://discussions.apple.com/thread/254691193?sortBy=rank"},

    {"user_prompt": "My dog refuses to go outside when it's raining.", 
     "url_to_check": "https://www.brilliantpad.com/blogs/news/dog-wont-poop-in-the-rain#:~:text=The%20sound%20of%20raindrops%2C%20thunder,also%20contribute%20to%20this%20fear."},

    {"user_prompt": "How much water should I drink every day?", 
     "url_to_check": "https://nutritionsource.hsph.harvard.edu/water/"},

    {"user_prompt": "I just got a flu shot. Can I still get the flu?", 
     "url_to_check": "https://mana.md/can-you-still-get-the-flu-if-you-get-a-flu-shot/"}
]

# Process each entry
results = []
for entry in data:
    result = validator.rate_url_validity(entry["user_prompt"], entry["url_to_check"])
    results.append(result)

# Print results in JSON format
print(json.dumps(results, indent=2))

