def convert_units(heroes, heights, weights):
    """Converts Hero's height from centemeters to inches and weight from kilograms to pounds."""
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data


def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis

import numpy as np

def get_publisher_heroes(heroes, publishers, desired_publisher):
    desired_heroes = []
    for i, pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])
    return desired_heroes

def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)
    desired_heroes = heroes_np[pubs_np == desired_publisher]
    return desired_heroes