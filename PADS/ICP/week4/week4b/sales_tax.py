def get_tax(total: float)->float:
    
    """
    accepts one argument and returns the tax value (6% of total)
    """

    return round(total*0.06, 2)

def get_total_after_tax(total: float)->float:

    """
    accepts one argument and returns (tota l +tax) value
    """

    return round(total + get_tax(total), 2)

