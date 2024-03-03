# This file contains the samples codes for "Exception Handling" section.

#%% Exception Handling (3)
try:
    # do something
    pass
except ValueError:
    # handle ValueError exception
    pass
except (TypeError, ZeroDivisionError):
    # handle TypeError and ZeroDivisionError
    pass
except:
    # handle all other exceptions
    pass
else:
    # do something if no error
    pass
finally:
    # do something regardless of whether there is error or no error
    pass

# %% Exception Handling (4)
try:
	num = int(input('Enter a number: '))
except:
	print('Not a number!')
else:
	print(f'You have entered {num}')
finally:
	print('Bye!')

# %% Exception Handling (5)
try:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line)
except OSError as e:
	print('Error: ', e)

# %% Exception Handling (6)
try:
	response = input('Enter something: ')
	assert response != ''
except AssertionError:
	print('You should enter something')
else:
	print(f'You have entered {response}')
