# question 1

def hello_name(user_name) :
    print("hello_"+user_name)
user_name = input('Nells: ')
hello_name(user_name)

# question 2

def first_odd() :
    for i in range(1,100) :
        if i % 2 !=0:
            print(i)
first_odd()


# question 3

def max_num_in_list(a_list) :
    maxium = A_list[0]
    for i in range(len(a_list)) :
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maxium
a_list = (10, 20, 30, 40, 50)
print(max_num_in_list(a_list))

# question 4

def is_leap_year(a_year) :

# question 5

def is_consecutive(a_list) :
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
# driver code
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list + [1,2,4,5]
print(is_consecutive(a_list))





