nums = input("Input: ")

nums = nums.strip("[]")           
numbers = [int(x) for x in nums.split(",")]

total = sum(n for n in numbers if n % 2 == 0)

print("Output:", total)
