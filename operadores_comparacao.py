x = z = y = False
n1 = n2 = 0

print("Digite um numero:")
n1 = int(input())
n2 = int(input("Digite outro numero:"))

x = n1==n2
print("São iguais?", x, '\n')

z = n1>n2
print(n1, 'é maior', n2, '?', z, '\n')

y = n1!=n2
print("São diferentes?" + str (y)) 