from matplotlib import pyplot as plt

def prime_number(number):
    if number !=1:
        for f in range(2, number):
            if number % f == 0:
                return
    else:
        return
    prime.append(number)

prime = []

for i in range(1, 10000):
    prime_number(i)
print(prime)

plt.plot(prime)
plt.show()