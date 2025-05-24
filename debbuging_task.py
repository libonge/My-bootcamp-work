 # Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # key was not was written full or Corrected variable name from 'k' to 'key'
# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",  # Use this quotation mark " " instead of these ' '
    "maggie": "(Pacifier Suck)"
}

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])  # make the keys as a list
