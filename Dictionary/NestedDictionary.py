IDs = [1,2,3]

emp = [{'name': 'sanju', 'job': 'Manager'},
           {'name': 'arav', 'job': 'clerk'},
           {'name': 'vinay', 'job': 'ceo'}]

result_set=dict(zip(IDs,emp))
print(result_set)