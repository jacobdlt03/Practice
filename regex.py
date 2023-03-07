import re

text = "A random string"

pattern = re.compile("[rdm]")

result = pattern.search(text)

print(result)