def fibonacci_maker(max_number):
    
    # Data initialization
    fibonacci_list=[0, 1]

    while fibonacci_list[-1]<max_number:
        new_value=fibonacci_list[-2]+fibonacci_list[-1]
        if new_value>=max_number:
            break
        fibonacci_list.append(new_value)

    return fibonacci_list

print(fibonacci_maker(100))