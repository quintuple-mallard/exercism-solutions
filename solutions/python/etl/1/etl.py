def transform(legacy_data):
    new_data={}
    for key in legacy_data.keys():
        for letter in legacy_data[key]:
            new_data[letter.lower()]=key
    return new_data
