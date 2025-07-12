"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    return list(wagons)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    wagon1, wagon2, *other = each_wagons_id
    fixed_wagons = [*other, wagon1, wagon2]
    locomotive, *the_rest = fixed_wagons
    fixed_wagons=[locomotive, *missing_wagons, *the_rest]
    return fixed_wagons

def add_missing_stops(route, **stops):
    route['stops']=[*stops.values()]
    print(route)
    return route
    


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    [*fixed_wagon_data]=zip(*wagons_rows)
    formatted_data=[]
    for wagon_tuple in fixed_wagon_data:
        wagon_list=list(wagon_tuple)
        formatted_data.append(wagon_list)
    return formatted_data