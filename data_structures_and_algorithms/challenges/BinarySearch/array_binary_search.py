def BinarySearch(arr,num):

  length_of_array = len(arr)
  
  index_of_the_list = length_of_array-1
  
  middle_idx= length_of_array // 2
  while arr[middle_idx] != num:
    if num > arr[index_of_the_list]:
      return -1
    else:
      if num == arr[middle_idx]:
        return middle_idx
      else:
        if num < arr[middle_idx]:
          middle_idx = middle_idx // 2
        elif num > arr[middle_idx]:
          middle_idx = index_of_the_list - middle_idx
  return middle_idx



if __name__=="__main__":
    print(BinarySearch([4,8,15,16,23,42], 15))
    print(BinarySearch([11,22,33,44,55,66,77], 90))