instructor = {
    'name': 'Eric',
    'age': 44,
    'handsome': True
}

instructor['car'] = 'Mazda_3'
print(instructor['car'])

cat = dict(name='shithead', age=4, color = 'rusty')
print(cat)

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)
print("\n")

for val in instructor.keys():
    print(val)

for k,v in instructor.items():
    print(f"Key is {k}, Value is {v}")



