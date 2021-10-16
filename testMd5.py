import hashlib

for number in range(0, 1000000):
    md5 = hashlib.md5(str(number).encode('utf-8')).hexdigest()
    if md5 == "140bf155d81b900c8b829d443805f530":
        print(number)

md5 = hashlib.md5(str(267869).encode('utf-8')).hexdigest()
print(md5)
print('end')
