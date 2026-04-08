full_stack = ["david","joshua","ibrahim"]
print(full_stack)
print(len(full_stack))
print(type(full_stack))
print(full_stack[0])
print(full_stack[0:3])
full_stack[1:3] = ["chop","beans"]
print(full_stack)
full_stack.insert(3,"rice")
print(full_stack)
full_stack.append("rice")
print(full_stack)

internet = ["Mtn","Glo","Etisalat"]
internet.extend(internet)
print(internet)
internet.remove("Mtn")
print(internet)