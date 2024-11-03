def list_division(my_list_1, my_list_2, list_length):
   new_list = []
   for i in range(list_length):
       result = 0
       try:
           if i < len(my_list_1) and i < len(my_list_2):
               result = my_list_1[i] / my_list_2[i]
           else:
               print("out of range")
       except TypeError:
           print("wrong type")
       except ZeroDivisionError:
           print("division by 0")
       finally:
           new_list.append(float(result) if isinstance(result, (int, float)) else 0)
   return new_list
