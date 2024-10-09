from collections import deque

def calc_deps(deps_matrix, init_dep):
    deps_queue = deque()
    loaded = deque()

    deps_queue.append(init_dep)
    loaded.append(init_dep)

    while deps_queue:
        curr_dep = deps_queue.popleft()
        for dep in deps_matrix[curr_dep]:
            if dep not in loaded:
                deps_queue.append(dep)
                loaded.append(dep)

    return loaded


packages = [
    [1,2],  # 0
    [3],    # 1
    [5],    # 2
    [],     # 3
    [5],    # 4
    [4]     # 5
]
dep_num = 0

print(calc_deps(packages, dep_num))

# test cases
# dep_num = 0 -> output = [0,1,2,3,5,4]
# dep_num = 4 -> output = [4,5]
# dep_num = 3 -> output = [3]
# dep_num = 2 -> output = [2,5,4]
