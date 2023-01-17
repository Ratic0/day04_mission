#7.1~3
year_lists = ['1996', '1997', '1998', '1999', '2000', '2001']
print(f'7.1~2 : {year_lists[2]}')
print(f'7.3 : {year_lists[-1]}')

#7.8~9
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(f'7.9 : {surprise}')

#7.10
num_list = []
for num in range(10) :
    if num % 2 == 0 :
        num_list.append(num)
print(f'7.10 : {num_list}')

#7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"
start1_list = []
print('7.11 : ')
for st1 in range(len(start1)) :
    print(f'{start1[st1].capitalize()}!', end=' ')
print(f'{rhymes[0][0].capitalize()}!')
print(f'{start2} {rhymes[0][1]}.')
