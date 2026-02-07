from linked_list import LinkedList

ll = LinkedList()

print("1. Добавляем элементы:")
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_ll()

print("\n2. Печать в обратном порядке:")
ll.print_ll_from_tail()

print("\n3. Вставляем по индексу:")
ll.insert_at_index(1, 15)
ll.print_ll()

print("\n4. Удаляем по значению:")
ll.remove_node_data(20)
ll.print_ll()

print("\n5. Длина списка:")
print(f"Длина: {ll.len_ll()}")

print("\n6. Поиск элементов:")
print(f"Содержит 15? {ll.contains_from_head(15)}")
print(f"Содержит 99? {ll.contains_from_head(99)}")

print("\n7. Поиск с выбором направления:")
print(f"Содержит 30 (с головы)? {ll.contains_from(30, from_head=True)}")
print(f"Содержит 30 (с хвоста)? {ll.contains_from(30, from_head=False)}")
