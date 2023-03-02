names = ["jenna", "susan", "jane", "sophia"]

l = []
for i in names:
    l.append(i)
print(l)

print([person for person in names])

l = []
for person in names:
    l.append(person + " dumped me")
print(l)

print([person + " dumped me" for person in names])

movies_and_ratings = {"interstellar": 9, "dark night": 8, "50 shades": 3, "fifty shades darker": 2, "fisty shades darkest": 1}

l = []
for movie in movies_and_ratings:
    if movies_and_ratings[movie] > 6:
        l.append(movie)
print(l)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])

#comment bc yeah i like to code and stuff lmao 