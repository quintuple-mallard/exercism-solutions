def proverb(*items, **last_line):
    proverb_text = []
    if len(items)==0:
        return []
    qualifier=last_line['qualifier']
    for i in range(len(items) - 1):
        proverb_text.append(f'For want of a {items[i]} the {items[i + 1]} was lost.')
    if qualifier is not None:
        proverb_text.append(f'And all for the want of a {qualifier} {items[0]}.')
    else:
        proverb_text.append(f'And all for the want of a {items[0]}.')
    return proverb_text
