# Divisible by 7? Skip
numbers = [12, 23, 34, 45, 56, 67]

for num in numbers:
    if num % 7 == 0:
        print(f"Divisible by 7: Skipping {num}")
        continue
    print(f"Processing: {num}")