# 列表加和
def get_sum(param_list):
    j = 0
    for i in param_list:
        j += i
    return j

# list1 = [2,3]
# list2 = [7, 5, 6]
# # print(f"sum of {list1}", get_sum(list1))
# # print(get_sum(list2))

# 计算列表数字范围中的所有偶数


def get_oushu(start, end):
    a = []
    for i in range(start, end):
        if i % 2 == 0:
            a.append(i)
    return a

# start = 0
# end = 27
# print (f"list of even between {start} and {end}", get_oushu(start, end))

# 移除列表中的多个元素


def exc(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista


# lista = [3, 5, 7, 9, 11, 13]
# listb = [7, 11]
# print(f"remove {listb} from {lista}, result: ", exc(lista, listb))

# 对列表去重复


def remove_elements(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result


# lista = [10, 20, 30, 10, 20]
# print(f"unique list: ", remove_elements(lista))


# 对简单列表排序
lista = [40, 20, 10, 30]
lista.sort(reverse=True)
# listb = sorted(lista, reverse=True)
listc = ['aa', 'bb', 'ee', 'cc']
listd = sorted(listc)
# print(f"order of {lista}")
# # print(f"ace order of {listb}")
# print(f"ace order of {listd}")


# 对学生成绩表排序
students = [
    {"sno": 101, "sname": "小张", "sgrade": 88},
    {"sno": 102, "sname": "小王", "sgrade": 65},
    {"sno": 103, "sname": "小李", "sgrade": 78},
    {"sno": 104, "sname": "小赵", "sgrade": 98},
]
students_sort = sorted(students, key=lambda x: x["sgrade"], reverse=True)

# print(students)
# print(students_sort)


# 读取成绩文件排序数据
def read_file():
    result = []
    with open("./student_grades.txt", encoding="utf-8") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
        return result

def sort_grades():
    return sorted(datas, key=lambda x: int(x[2]), reverse=True)

def write_file(datas):
    with open("./student_grades_output", "w", encoding="utf-8") as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")

# 1.读取文件
datas = read_file()
print(datas)
# 2.排序数据
datas = sort_grades()
print(datas)
# # 3.写出文件
write_file(datas)