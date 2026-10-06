hold = float(input())
n = int(input())
cnt = 0
cnt_err = 0
max = -100000
ave = 0
for i in range(n):
    inp = input()
    if inp == 'error':
        cnt_err += 1        
    else:
        inp = float(inp)
        if inp > hold:
            cnt += 1
        ave += inp
        if inp > max:
            max = inp
    
print(n)
print(cnt_err)
print(cnt)
print(f'{max:.1f}')
print(f'{(ave / (n - cnt_err)):.1f}')
