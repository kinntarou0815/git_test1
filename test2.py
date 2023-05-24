from math import sqrt
for n in range(9,0,-1):
    root = sqrt(n)
    if root == int(root):
        print(root)
        break

word = "ダミー"
while True:
    word = input("単語を入力してください")
    print(not word)
    if  not word:
        break
    print("単語は"+word+"でした")
