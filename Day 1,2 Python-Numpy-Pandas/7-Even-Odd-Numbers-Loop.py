even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for i in range(1,50):
    if i%2==0:
        even_sum+=i
        even_count+=1
        print("Even number:", i)
    else:
        odd_sum+=i
        odd_count+=1
        print("Odd number:", i)

print("Even Count:", even_count)
print("Even Sum:", even_sum)

print("Odd Count:", odd_count)
print("Odd Sum:", odd_sum)

print("Total Count:", even_count + odd_count)
print("Total Sum:", even_sum + odd_sum)

print("Average:", (even_sum + odd_sum)/(even_count + odd_count))