test_list =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]

print("The original list : ",test_list)
res = list(set(val for dic in test_list
                for val in dic.values()))

# printing result
print("The unique values in list are : " + str(res))