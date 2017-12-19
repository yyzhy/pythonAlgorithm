#function for find min or max value.
def binFind(list, val):
    mid = int(len(list) / 2)
    found = False
    if mid == 0:
        return found
    if list[mid] == val:
        found = True
        return found
    elif list[mid] < val:
        return binFind(list[mid:], val)
    elif list[mid] > val:
        return binFind(list[:mid], val)
