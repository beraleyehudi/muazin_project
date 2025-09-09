one_string = 'Genocide,War Crimes,Apartheid,Massacre,Nakba,Displacement,Humanitarian Crisis,Blockade,Occupation,Refugees,ICC,BDS'
two_string = 'Freedom Flotilla,Resistance,Liberation,Free Palestine,Gaza,Ceasefire,Protest,UNRWA'
one = one_string.lower().split(',')
two = two_string.lower().split(',')

print(one,'\n', two)

some_string = ''

def performances_and_variety(hostile_words, text) -> dict:
    counter = 0
    lis = []
    dic = {'performances_precent':0, 'variety_precent':0}
    for i in text.split(','):
        if f'{i}' in hostile_words:
            counter += 1
            if not f'{i}' in lis:
                lis.append(i)

    dic['performances_precent'] = counter/len(text.split(','))
    dic['variety_precent'] = len(lis) / len(hostile_words)
    return dic
def calculate(hostile_words_1, hostile_words_2, text):
    hostile_words_1_data = performances_and_variety(hostile_words_1, text)
    hostile_words_2_data = performances_and_variety(hostile_words_2, text)

    percentage_of_dangerous_words_performances = hostile_words_1_data['performances_precent'] + hostile_words_2_data['performances_precent']
    performance_diversity_percentage = hostile_words_1_data['variety_precent'] * hostile_words_2_data['variety_precent']


    return percentage_of_dangerous_words_performances * performance_diversity_percentage

concatenation = ','.join(one) + ',' + ','.join(two)
print(concatenation)
my = 'genocide,war crimes,apartheid,massacre,nakba,displacement,humanitarian crisis'
print(calculate(one, two, concatenation))



print(performances_and_variety(one, concatenation))
print(performances_and_variety(two, concatenation))