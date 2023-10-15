# find the geometric mean of n numbers 
import math

def geometric_mean(numbers):
    if len(numbers) == 0:
        return None 
    product = 1
    for number in numbers:
        product *= number

    geometric_mean = math.pow(product, 1/len(numbers))
    return geometric_mean


numbers = [4,5, 4, 8]
result = geometric_mean(numbers)
print("Geometric Mean:", {result})