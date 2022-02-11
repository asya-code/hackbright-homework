"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    data = open(filename)
    species = []
    for line in data: 
        line = line.strip()
        raw_profile = line.split("|")
        animal = raw_profile[1]
        species.append(animal)
    species = set(species)
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    data = open(filename)
    villagers = []
    for line in data: 
        line = line.strip()
        raw_profile = line.split("|")
        animal = raw_profile[1]
        name = raw_profile[0]
        if search_string = "All":
            villagers.append(name)

        if animal == search_string:
            villagers.append(name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    data = open(filename)
    villagers = []
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    for line in data: 
        line = line.strip()
        raw_profile = line.split("|")
        hobby = raw_profile[3]
        name = raw_profile[0]
        if hobby == "Fitness":
            fitness.append(name)
        if hobby == "Nature":
            nature.append(name)
        if hobby == "Education":
            education.append(name)
        if hobby == "Music":
            music.append(name)
        if hobby == "Fashion":
            fashion.append(name)
        if hobby == "Play":
            play.yappend(name)
    villagers.append(fitness)
    villagers.append(nature)
    villagers.append(education)
    villagers.append(music)
    villagers.append(fashion)
    villagers.append(play)

    return villagers


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
file_name.close()