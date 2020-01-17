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




def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        for pairings in melon.pairings:
            print(melon.name, "pairs with", pairings)


# print_pairing_info(result)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    code_dict = {}

    for melon in melon_types:
        code_dict[melon.code] = melon.name

    return code_dict



    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_num, harvester):
        """Initialize a melon."""

        # Fill in the rest


        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_num = field_num
        self.harvester = harvester
        
    def is_sellable(self, shape_rating, color_rating, field_num):

        if (shape_rating > 5) and (color_rating > 5) and (field_num != 3):

            return True 

        else:

            return False
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_objects = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')

    melon_objects.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')

    melon_objects.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')

    melon_objects.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')

    melon_objects.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')

    melon_objects.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')

    melon_objects.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')

    melon_objects.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')

    melon_objects.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melon_objects.append(melon_9)

    return melon_objects




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable(melon.shape_rating, melon.color_rating, melon.field_num) is True:
            print(f"Harvested by {melon.harvester} from Field {melon.field_num} (CAN BE SOLD)")

        else:
            print(f"Harvested by {melon.harvester} from Field {melon.field_num} (NOT SELLABLE)")

    # Fill in the rest 

melon_types = make_melon_types()
# melon_dict = make_melon_type_lookup(melon_types)
melon_objects = make_melons(melon_types)

get_sellability_report(melon_objects)