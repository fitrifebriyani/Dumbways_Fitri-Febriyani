
def productArray(arr, n):
    if (n == 1):
        print(0)
        return

    kiri = [0]*n
    kanan = [0]*n

    prod = [0]*n

    kiri[0] = 0
    kanan[n-1]=0

    for i in range(1,n):
        kiri[i] = arr[i-1] + kiri[i-1]

    for j in range(n-2, -1, -1):
        kanan[j] = arr[j+1] + kanan[j+1]

    for i in range(n):
        prod[i] = kiri[i] + kanan[i]

    for i in range(n):
        print(prod[i])

    print("maka angka terbesarnya adalah: ",max(prod))
    print("maka angka terkecilnya adalah: ",min(prod))

arr = [4,9,10,13,21]
n = len(arr)
print("the product array  is: ")
productArray(arr, n)
