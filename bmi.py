def convert_to_meters(feet, inches):
    return (feet*12 + inches)*0.025


def convert_to_kg(weight):
    return weight*.45


# bmi is kg/(m)^2
def bmi(height_f, height_i, weight):
    height_m = convert_to_meters(height_f, height_i)

    kg = convert_to_kg(weight)

    return kg/height_m**2
