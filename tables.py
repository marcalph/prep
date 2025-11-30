from tabulate import tabulate


# Generate the standard Fibonacci sequence
def fibonacci_sequence(n):
    sequence = [(0, 0), (1, 1)]
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
        sequence.append((i, b))
    return sequence


# Generate the first 10 Fibonacci numbers
sequence = fibonacci_sequence(10)

# Transpose the data for better visualization
print(sequence)
print(*sequence)
indices, values = zip(*sequence)

# Correctly formatted transposed table
transposed_table = [("Index", *indices), ("Fib(n)", *values)]

# Print the transposed table
print(tabulate(transposed_table, tablefmt="grid"))
