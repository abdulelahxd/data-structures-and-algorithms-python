def insertShiftArray(list_two,val):
  Lis = list_two.copy()
  Lis.sort()
  length = 0
  while True:
      try:
          Lis[length]
      except IndexError:
          break
      else:
          length += 1
          continue
  length_of_list = length
  print(length_of_list)
  i=0
  value='value'
  
  # to add new array with spesific numer of index
  new_list=[value]*(length_of_list+1)
  print(new_list)
  while i<length_of_list:
    if Lis[i]<val:
      new_list[i]=Lis[i]
    elif Lis[i]>val:
      new_list[i+1]=Lis[i]
      if new_list[i] == value:
        new_list[i]= val
    elif Lis[i]>val:
      new_list[i]==val
    
    i+=1
  
  return new_list

print(insertShiftArray([2,4,6,8], 5))
print(insertShiftArray([4,8,15,23,42], 16))