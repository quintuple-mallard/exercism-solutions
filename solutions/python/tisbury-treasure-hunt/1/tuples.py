"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[-1]


def convert_coordinate(coordinate):
    return (coordinate[0],coordinate[1])


def compare_records(azara_record, rui_record):
    if convert_coordinate(azara_record[1])==rui_record[1]:
        return True
    return False

def create_record(azara_record, rui_record):
    if compare_records(azara_record,rui_record):
        return (azara_record[0],azara_record[1],rui_record[0],rui_record[1],rui_record[2])
    return "not a match"

def clean_up(combined_record_group):
    combined_records = tuple(tuple([i[0]])+i[2:] for i in combined_record_group)
    report = "\n".join(str(record) for record in combined_records) + "\n"
    return report