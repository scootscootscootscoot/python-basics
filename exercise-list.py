#play with for loops




#create a list
random_list = []
print("Your list:", random_list)

random_list.append("alpha")
random_list.append("beta")
random_list.append("delta")
random_list.append("epsilon")
random_list.append("gamma")
random_list.append("zeta")


#use a loop to iterate through the list 
print("Heres a random list of things")
for task in random_list:
    print("- ", task)


done_task = random_list.pop(2)
print("You removed:", done_task)
print("removed list after removal:", random_list)