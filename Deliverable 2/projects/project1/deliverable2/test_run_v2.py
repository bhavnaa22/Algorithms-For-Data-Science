from deliverable2 import *

# Instantiate the URLValidator class
validator = URLValidator()

# Define user prompt and URL
user_prompt = "I just finished watching a horror movie alone at night."
url_to_check = "https://www.quora.com/How-does-it-feel-watching-a-horror-film-alone-at-night"

# Run the validation
result = validator.rate_url_validity(user_prompt, url_to_check)

# Print the results
import json
print(json.dumps(result, indent=2))
