word = ["this","is","an","world"]
for words in word:
    print(words)

name = ""
while not name:
    name = input("名前を入力してください")
    print(f"こんにちは{name}さん")
    d = {"s":2,"a":4}
    for k,v in d.items():
        print(k+"の値は"+ str(v)+"です")