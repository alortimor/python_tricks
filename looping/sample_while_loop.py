#!/usr/bin/python3

sample_1 = "some_name = the_value"
sample_2 = "Peter = Koukoulis"

position = -1
for position in range (len(sample_2)):
    if sample_2[position] in '=:':
        break


if position == -1:
    print("name=", None, "value=", None)
elif not (sample_2[position] == ':' or sample_2[position] == '='):
    print('name=', None, 'value=', None)
else:
    print('name=', sample_2[:position], 'value=', sample_2[position+1:])


if len(sample_2) > 0:
    name, value = sample_2, None
else:
    name, value = None, None

for position in range(len(sample_2)):
    if sample_2[position] in '=:':
        name, value = sample_2[:position], sample_2[position:]

print('name=', name, 'value=', value)

for position in range(len(sample_2)):
    if sample_2[position] in '=:':
        name, value = sample_2[:position], sample_2[position:]
        break
else:
    if len(sample_2) > 0:
        name, value = sample_2, None
    else:
        name, value = None, None


print('name=', name, 'value=', value)
