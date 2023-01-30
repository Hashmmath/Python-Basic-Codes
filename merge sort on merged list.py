def merge_sort(list1, list2):
    merged_list = list1 + list2
    if len(merged_list) > 1:
        mid = len(merged_list)//2
        left_list = merged_list[:mid]
        right_list = merged_list[mid:]
        merge_sort(left_list, right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                merged_list[k] = left_list[i]
                i += 1
            else:
                merged_list[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            merged_list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            merged_list[k] = right_list[j]
            j += 1
            k += 1
    return merged_list
