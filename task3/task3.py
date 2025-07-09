# Задание 3: report.json

import json

file1, file2, file3 = [el for el in input().split()]
with open(file1, 'r') as file:
    tests_structure = json.load(file)


with open(file2, 'r') as file:
    values_list = json.load(file)
values_list = values_list["values"]


def update_test_values(tests_structure, values_list):
    node_map = {}

    def traverse(nodes):
        for node in nodes:
            node_map[node['id']] = node

            if 'values' in node:
                traverse(node['values'])

    traverse(tests_structure['tests'])

    for item in values_list:
        if int(item['id']) in node_map:
            node_map[item['id']]['value'] = item['value']

    return tests_structure

report = update_test_values(tests_structure, values_list)

with open(file3, 'w') as file:
    json.dump(report, file)
