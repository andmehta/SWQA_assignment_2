def convert_to_meters(feet, inches):
    return (feet*12 + inches)*0.025


def convert_to_kg(weight):
    return weight*.45


# bmi is kg/(m)^2
def bmi(height_f, height_i, weight):
    height_m = convert_to_meters(height_f, height_i)

    kg = convert_to_kg(weight)

    bmi_value = kg/height_m**2
    if  0 < bmi_value <= 18.5:
        category = "Underweight"

    if 18.5 < bmi_value < 25:
        category = "Normal"

    if 25 >= bmi_value < 30:
        category = "Overweight"

    if bmi_value >= 30:
        category = "Obese"
    return bmi_value, category
