print ("Digite um número entre 0 e 1023: ")
n = int(input())
d = n % 2
dec = 1
bin = d
quoc = n // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

d = quoc % 2
dec *= 10
bin += d * dec
quoc = quoc // 2

print (n, "decimal em binário é", bin)