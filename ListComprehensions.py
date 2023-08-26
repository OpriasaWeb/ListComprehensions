
num_of_insects = int(input("Please enter the number of insects: "))

# Basic coding - more on mathematical
nums = [num_of_insects*2**i for i in range(12)]

print(nums)

# Hard coding - more on logical
for i in range(12):
  print(num_of_insects)
  num_of_insects = num_of_insects * 2
  
