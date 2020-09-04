import re

# Use a helper function to find the words
def helper_func(partterns, phrase):

    for pat in partterns:
        print('Looking for the parttern {}'.format(pat))
        print(re.findall(pat,phrase))
        print('\n')

my_phrase = 'ssdd...sd...s....sssdddd...sddd...sssdd...sdd....ssssssdddddd'

my_pat = ['sd+']

# helper_func(my_pat, my_phrase)

def my_func():
    print('I am in different file')