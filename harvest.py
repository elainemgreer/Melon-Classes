############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = True
        self.is_bestseller = True
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')

    muskmelon.add_pairing('mint')

    all_melon_types.append(muskmelon)



    casaba = MelonType('cas', 2003, 'orange', True, False, 'Casaba')

    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    all_melon_types.append(casaba)



    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')

    crenshaw.add_pairing('proscuitto')

    all_melon_types.append(crenshaw)



    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, 
                                  'Yellow Watermelon')

    yellow_watermelon.add_pairing('ice cream')

    all_melon_types.append(yellow_watermelon)


    return all_melon_types


result = make_melon_types()
print(result)


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        for pairings in melon.pairings:
            print(melon.name, "pairs with", pairings)


print_pairing_info(result)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    code_dict = {}

    for melon in melon_types:
        code_dict[melon.code] = melon.name

    return code_dict

result = make_melon_type_lookup(result)
print(result)

    # Fill in the rest

# ############
# # Part 2   #
# ############

# class Melon(object):
#     """A melon in a melon harvest."""

#     # Fill in the rest
#     # Needs __init__ and is_sellable methods

# def make_melons(melon_types):
#     """Returns a list of Melon objects."""

#     # Fill in the rest

# def get_sellability_report(melons):
#     """Given a list of melon object, prints whether each one is sellable."""

#     # Fill in the rest 



