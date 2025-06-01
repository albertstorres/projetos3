def calculate_deposit (weight, price, bonus):
    weight_bonus = 1
    total = 0

    if weight >= 5 and weight < 10:
        weight_bonus = 50
    elif weight >= 10 and weight < 20:
        weight_bonus = 100
    elif weight >= 20 and weight < 50:
        weight_bonus = 150
    else:
        weight_bonus = 200

    total = weight * price * bonus * weight_bonus

    return total