import markovify

# Get raw text as string.
with open("prop.txt", encoding='utf8', errors='ignore') as f:
    text = f.read()
# please put your own *.txt file in the same folder as markgen.py

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(10000):
    print(text_model.make_short_sentence(140))
