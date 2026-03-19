A = int(input())
B, C, D = map(int, input())

ans1 = A * D
ans2 = A * C
ans3 = A * B
ans4 = (ans1 + ans2*10 + ans3*100)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
