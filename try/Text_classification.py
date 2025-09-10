one_string = 'Genocide,War Crimes,Apartheid,Massacre,Nakba,Displacement,Humanitarian Crisis,Blockade,Occupation,Refugees,ICC,BDS'
two_string = 'Freedom Flotilla,Resistance,Liberation,Free Palestine,Gaza,Ceasefire,Protest,UNRWA'
one = one_string.lower().split(',')
two = two_string.lower().split(',')
import re

print(one,'\n', two)

some_string = ''

def performances_and_variety(hostile_words, text) :
    counter = 0
    lis = []
    dic = {'performances_precent':0, 'variety_precent':0}
    for i in text.split():
        if f'{i}' in hostile_words:
            counter += 1
            if not f'{i}' in lis:
                lis.append(i)

    dic['performances_precent'] = counter/len(text.split())
    dic['variety_precent'] = len(lis) / len(hostile_words)
    return dic


def calculate(hostile_words_1, hostile_words_2, text):
    hostile_words_1_data = new_shape(hostile_words_1, text)
    hostile_words_2_data = new_shape(hostile_words_2, text)

    percentage_of_dangerous_words_performances = hostile_words_1_data['performances_precent']/2 + hostile_words_2_data['performances_precent']
    performance_diversity_percentage = hostile_words_1_data['variety_precent'] * hostile_words_2_data['variety_precent']


    return percentage_of_dangerous_words_performances * performance_diversity_percentage

concatenation = ','.join(one) + ',' + ','.join(two)
print(concatenation)
my = "the resistance Massa Humanitarian Crisis of the people  Humanitarian Crisis in Gaza is incredible even in the face of Massacre they hold on to Hope true and hope itself is a form of resistance under apartheid and occupation the freedom flotilla is another symbol Ordinary People challenging the blockade with humanitarian Aid and when governments fail International protests step in from universities to City squares people chant for a ceasefire and Liberation and with BTS we channel that energy into real pressure boycott and divestment may seem small but combined their powerful exactly every voice every action adds up free Palestine isn't just a slogan it's a global demand"
my_2 = "the protests are growing Millions demanding a ceasefire chanting for justice people see the occupation for what it is apartheid exactly Liberation movements always begin with protest that's how power shifts and BDS gives those protests economic and cultural teeth the blockade can't erase resilience resistance is alive and so is Hope"
# print(calculate(one, two, concatenation))
# print(calculate(one, two, my_2))

a = 'Humanitarian Crisis'
print(re.findall(rf'\b{a}\b', my) )
print()

def new_shape(bank, text):
    performance_counter = 0
    variety_counter = 0
    dic = {}

    for word_from_bank in bank:
        performances = re.findall(rf'\b{word_from_bank}\b', text)
        if performances:
            variety_counter += 1
            performance_counter += len(performances)

    dic['performances_precent'] = performance_counter / len(text.split())
    dic['variety_precent'] = variety_counter / len(bank)
    return dic


print(performances_and_variety(two, my))
print(new_shape(one, my))
print(calculate(one, two, my_2))