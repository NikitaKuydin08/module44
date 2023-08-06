#при помощи set делаем строку с в МНОЖЕСТВО, ГДЕ ВЫВОДЯТСЯ ТОК УНИКАЛЬНЫЕ ВЕЩИ
"""def strcounter(s): #O (N*M) M = кол-во уник элементов, n = кол-во всех символов = асимптотическая сложность
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sum == sub_sym:
                count+=1
        print(sym, count)
strcounter('dadada')
"""
"""def strcounter(s): #O (N*2)n = кол-во всех символов = асимптотическая сложность - не очень хороший, плохой
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sum == sub_sym:
                count+=1
        print(sym, count)
strcounter('dadada')"""
def strcounter(s): #O(N) - линейная, скок символов - например, 3 и работает (обрабатывает ток 3 раза в фор, принт не влияет так сильно)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)
strcounter('adadaad')
print(12132)