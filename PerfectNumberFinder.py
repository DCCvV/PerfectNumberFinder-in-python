import time
import os

def is_perfect(n):
    if n <= 0:
        return False    
    sum_of_div = 0
    
    
    for i in range(1, n):
        if n % i == 0:
            sum_of_div += i     

    return sum_of_div == n



def find_in_range(start, end):
    perfect_numbers = []
    
    for num in range(start, end + 1):
        #print(num) just prints the number that it is checking
        persentage = num / (end / 100)
        if is_perfect(num):
            perfect_numbers.append(num)
        print(f'Completion Progress: |{persentage}%|')
        #os.system("clear")
        #print(f"Number {num} DONE!")
    return perfect_numbers


start_range = 1

end_range = int(input('When to END search: '))

start_time = time.time()
found_perfect_numbers = find_in_range(start_range, end_range)
end_time = time.time()
print("FINISHED! \n")
print(f"Elapsed Time: {end_time - start_time} || Numbers searched: {end_range}")
print(f"Perfect numbers between {start_range} and {end_range}: {found_perfect_numbers}")

#now ofc this could be better but im too busy at the moment
