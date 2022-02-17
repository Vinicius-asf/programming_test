def print_descending_order_recursively(n:int):
    string_result = str(n)
    if n > 0:
        string_result = string_result+print_descending_order_recursively(n-1)
        return string_result
    else:
        print(string_result)

