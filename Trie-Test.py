dictionary = open("NASPA-Dictionary.txt","r")
dicts = dictionary.readlines()
the_dictionary_to_rule_them_all = []
for line in dicts:
    word = line.strip()
    if len(word) >= 4:
        the_dictionary_to_rule_them_all.append(line.strip())

print(the_dictionary_to_rule_them_all)