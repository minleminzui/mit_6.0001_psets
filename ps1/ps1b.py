
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:​ "))
portion_down_payment = total_cost * 0.25
current_savings = 0.0
r = 0.04
month = 0

while current_savings <  portion_down_payment:
    current_savings *= (1 + r / 12)
    # if(month % 6 == 0): #the piece of code for raising salary should not put there
    #     annual_salary *= (1 + semi_annual_raise) #because 'month' being zero wil raising salary
    current_savings += (annual_salary / 12 * portion_saved)
    month += 1
    if(month % 6 == 0):
        annual_salary *= (1 + semi_annual_raise)


print("Number of months: ", month)