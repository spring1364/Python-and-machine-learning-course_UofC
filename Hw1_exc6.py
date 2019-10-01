def decode(run_length_list):
    """
    Run-length encoding is a simple data compression technique that can be effective when
    repeated values occur at adjacent positions within a list. Compression is achieved by
    replacing groups of repeated values with one copy of the value, followed by the number
    of times that the value should be repeated.
    :param run_length_list: an encoded list
    :return: decoded list
    """
    if not run_length_list:
        return ""
    index = run_length_list[0]
    frequency = run_length_list[1]
    decomp = index * frequency + decode(run_length_list[2:])
    return decomp


run_length_list = ["A", 5, "B", 4, "A", 6, "D", 2]
print("Run length encoded list: ")
print(run_length_list)
print("Run length decoded list: ")
print(list(decode(run_length_list)))
