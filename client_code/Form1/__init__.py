from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def btn_sapxep_click(self, **event_args):
        # Nhận danh sách từ text box và chuyển đổi thành danh sách số nguyên
        arr_input = self.box_nhapphantu.text.split()
        
        # Kiểm tra số lượng phần tử
        if len(arr_input) != int(self.box_nhapn.text):
            raise ValueError("Lỗi: Số lượng phần tử không đúng!")
            return  # Dừng việc sắp xếp nếu số lượng không đúng

        arr = [int(x) for x in arr_input]

        # Sắp xếp và hiển thị kết quả
        self.box_truockhisapxep.text = "Dãy số nguyên trước khi sắp xếp: " + ' '.join(map(str, arr))

        sorted_arr = arr.copy()
        self.insertion_sort(sorted_arr)
        self.box_InsertionSort.text = "Insertion Sort: " + ' '.join(map(str, sorted_arr))

        sorted_arr = arr.copy()
        self.selection_sort(sorted_arr)
        self.box_SelectionSort.text = "Selection Sort: " + ' '.join(map(str, sorted_arr))

        sorted_arr = arr.copy()
        self.bubble_sort(sorted_arr)
        self.box_BubbleSort.text = "Bubble Sort: " + ' '.join(map(str, sorted_arr))

        sorted_arr = arr.copy()
        self.merge_sort(sorted_arr)
        self.box_MergeSort.text = "Merge Sort: " + ' '.join(map(str, sorted_arr))

    # Hàm sắp xếp chèn
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    
    # Hàm sắp xếp lựa chọn
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    
    # Hàm sắp xếp nổi bọt
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    
    # Hàm sắp xếp trộn
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
    
            self.merge_sort(left_half)
            self.merge_sort(right_half)
    
            i = j = k = 0
    
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
    
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
    
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
