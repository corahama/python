def sort_array(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sort_array(stack)
    insert_element_in_ordered_stack(stack, top)
    return stack

def insert_element_in_ordered_stack(stack, value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insert_element_in_ordered_stack(stack, value)
    stack.append(top)

if __name__ == '__main__':
    print(sort_array([-5, 2, -2, 4, 3, 1]))
