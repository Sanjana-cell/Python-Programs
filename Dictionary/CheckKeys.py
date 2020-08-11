emp={"name":"sanjana","course":"mca","year":3,"fee":60000}
key_set1={"name","course"}
key_set2={"year","id"}
if emp.keys() >= key_set1:
    print("IS",key_set1,"present ? ture")
else:
    print("IS",key_set1,"present ? false")
if emp.keys() >= key_set2:
    print("IS", key_set2, "present ? ture")
else:
    print("IS", key_set2, "present ? false")