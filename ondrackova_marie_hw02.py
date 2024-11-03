import pandas as pd
import json
netflix_list = [] #načtení seznam řádků vstupního souboru (seznam seznamů)
with open( 'netflix_titles.tsv', encoding = 'utf-8') as file:
     for line in file:
        line = line.strip().split('\t')
        netflix_list.append(line)     

netflix_list = netflix_list[1:] # odmazání záhlaví

output = [] # seznam na slovníky

for line in netflix_list:
    netflix_dict = {}
    netflix_dict['title']  = line[2]
    directors = line[15].split(',') # vytvoření seznamu režisérů ze stringu
    netflix_dict['director'] = directors
    actors = line[16].split(',')
    netflix_dict['cast'] = actors 
    netflix_dict['decade'] = line[5][:3] + '0'
    genre_list = line[8].split(',')
    netflix_dict['genre'] = genre_list
    output.append(netflix_dict)  


with open('hw02_output.json','w', encoding='utf-8') as newfile:
    json.dump(output, newfile, indent=4)          
