t = int(input())
for tc in range(1, t+1):
    binary = input()
    
    ans = []
    for i in range(0, 70, 7):
        num_str = binary[i:i+7]
        num = int(num_str, 2)
        ans.append(num)
        
    print(f"#{tc}", *ans)