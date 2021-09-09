
annual_salary = float(input("Enter the starting salary: "))
portion_saved = .5
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = total_cost * 0.25
current_savings = 0.0
r = 0.04
month = 36

def sum_36(portion_saved, annual_salary, current_savings):
    for month in range(1, 37):#not range(36). there is a hidden bug, for loop and while loop differ in the first 'month'.In for loop, the first month must be 1
        current_savings *= (1 + r / 12) 
        current_savings += (annual_salary / 12 * portion_saved)
        if(month % 6 == 0 and month != 0):
            annual_salary *= (1 + semi_annual_raise)
    return current_savings

if(sum_36(1, annual_salary, current_savings) < portion_down_payment - 100):
    print("It is not possible to pay the down payment in three years.")
else:
    low = 0
    high = 10000
    step = 1
    portion_saved = int((low + high )) / 2
    t_sum = sum_36(portion_saved / 10000, annual_salary, current_savings)
    while abs(t_sum - portion_down_payment) > 100:
        if t_sum < portion_down_payment - 100:
            low = portion_saved
        elif t_sum > portion_down_payment + 100:
            high = portion_saved

        step += 1
        portion_saved = int((low + high ) / 2)
        t_sum = sum_36(portion_saved / 10000, annual_salary, current_savings)
    print("Best savings rate: ", portion_saved / 10000)
    print("Steps in bisection search: ", step)
