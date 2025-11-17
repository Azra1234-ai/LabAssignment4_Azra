def cm_to_inches(cm):
    """
    Converts centimeters to inches.
    1 inch = 2.54 centimeters.
    """
    return cm / 2.54
if __name__ == "__main__":
    
    cm_value = float(input("Enter length in centimeters: "))
    inches_value = cm_to_inches(cm_value)
    print(f"{cm_value} cm is equal to {inches_value:.2f} inches.")
