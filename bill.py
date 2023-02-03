# 發票兌獎
win = open('win.txt').read().split()
mine = open('mine.txt').read().split()

for i, num in enumerate(mine):
    if num in win :
        print("第",i+1,"張發票中獎",num, '!')