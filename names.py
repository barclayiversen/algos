test_case = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

def nameList(names):
    length = len(test_case)
    position_in_list = 0
    final_string = ""
    for name in names:
        #print position_in_list
        if len(names) - position_in_list == 2:
            for name2 in names[position_in_list:]:
                final_string += " " + name2['name'] + ' & ' + names[-1]['name']
                print final_string
                return final_string
        final_string += " " + name['name']+","
        print final_string
        position_in_list +=1
    
nameList(test_case)