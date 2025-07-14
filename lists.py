
# list example
list = [12, "hello", 24, True, False, True, 16.0]
# index [0]   [1]    [2]  [3]   [4]    [5]   [6]
        
print(list)

# length of said list
ans = lens(list)

print(list)

# getting an element
ans = list[1]
print(ans)

# gets an element from the last index
ans = list[-1]
print(ans)

# getting a subselection of items
ans = list[0:4]  #first number is starting index, second number is last index
print(ans)

ans = list[:4] # from starting up to 4 index
print(ans)

ans = list[2:] # from 2 up to last index
print(ans)


ans = list[1:6:2] # from 1 to 6 with 2 steps
print(ans)

ans = list[-4:] # 4 from the back of the list
print(ans)

ans = list[::-1] # reversing the direction of the list
print(ans)

