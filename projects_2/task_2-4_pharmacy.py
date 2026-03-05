count_of_whole_capsules = int(input("Введите общее количество капсул: "))
capacity_of_one_package = int(input("Введите вместимость одной упаковки: "))

count_of_fulled_packeges = count_of_whole_capsules // capacity_of_one_package
count_of_remaining_capsules = count_of_whole_capsules % capacity_of_one_package

print(f"Общее количество произведенных капсул: {count_of_whole_capsules}\n Вместимость одной упаковки: {capacity_of_one_package}\n\n Отчет фасовочного цеха\n Полных упаковок: {count_of_fulled_packeges}\n Остаток капсул: {count_of_remaining_capsules}")