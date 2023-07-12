from enum import Enum


class Category(Enum):
    Loan = 11
    PropertyTax = 12
    Utility = 13
    Subscription = 21
    Grocery = 31
    Restaurant = 32
    Snacks = 33
    Fashion = 41
    Beauty = 42
    Household = 43
    OtherHousehold = 44
    Sports = 51
    Movie=52
    OtherEntertainment=53
    Car = 61
    OtherTransportation = 62
    Travel = 71
    PreventiveMedicare = 81
    TherapeuticMedicare = 82
    Social = 91
    Cat = 101
    Other = 111


def guess_category_based_on_keyword(category_dict, description):
    for keyword in category_dict:
        if keyword in description.lower():
            return category_dict[keyword]
    return Category.Other
