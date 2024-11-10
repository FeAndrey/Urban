def count_calls():
    global calls
    calls+=1

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    boolean_ = False
    for i in range(len(list_to_search)):
        if string.casefold() == list_to_search[i].casefold():
            boolean_ = True
        else:
            boolean_ = False
    return boolean_

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

