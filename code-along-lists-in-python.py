#create an empty list

todo_list = []
print("Your todo list:", todo_list)

#append items to the list

todo_list.append("Buy Groceries")
todo_list.append("finish homework")
todo_list.append("call mom")


print("updated list:", todo_list)

#insert an item

todo_list.insert(1, "Pay bills")
print("After inserting an item:", todo_list)


#using indexes and slicing

print("first task:", todo_list[0])
print("last two tasks:", todo_list[-2:])

#mark a task as done

done_task = todo_list.pop(2)
print("You completed:", done_task)
print("Todo list after removal:", todo_list)


#update an existing task
print(todo_list[1])
todo_list[1] = "buy groceries and snacks"
print("updated todo list value:", todo_list[1])

#print a task list

print("here's what you still need to do:")
for task in todo_list:
    print("- ", task)


