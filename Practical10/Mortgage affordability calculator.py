def can_buy_house(value, salary):
    max_house_value = 5 * salary
    if value <= max_house_value:
        return 'Yes'
    else:
        return 'No'
    house_value = 180000
    annual_salary = 35000
    result = can_buy_house(house_value, annual_salary)
    print(result)  # Output: Yes