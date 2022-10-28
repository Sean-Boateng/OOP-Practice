### Print from a function ###

def print_my_string():
    my_string = "Hello Seaborgium!"
    print(my_string)
print_my_string()

### Return from a function ###

def return_my_string():
    my_string = "Hello Seaborgium!"
    return my_string

returned_string = return_my_string()
print(returned_string)

### Find the area of a rectangle ###

def find_the_area(num_one, num_two):
        area = int(num_one) * int(num_two)
        return area

user_width_input = input("What is the width of the rectangle?")
user_height_input = input("What is the height of the rectangle?")

area_product = find_the_area(user_width_input, user_height_input)
print(area_product)

### Validate password ###

def validate_password():
    valid_password = False
    status = ''
    while valid_password == False:
        user_password_input = input("Please enter your password")
        if user_password_input != "password123":
            print("Invalid Password")
            status = "Invalid"
        else:
            valid_password = True
            status = "Valid"
    return status


login_result = validate_password()
print(login_result)


### Find sum of list ###

def find_the_sum(my_list):
    list_sum = 0
    for num in my_list:
        list_sum += num
    return list_sum

num_list = [33,44,17,16]
sum = find_the_sum(num_list)
print(sum)