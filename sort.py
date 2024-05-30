def sort(data):
  for i in range(len(data)-1):
    min_idx = i
    for j in range(i+1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j
    data[i], data[min_idx] = data[min_idx], data[i]
  return data