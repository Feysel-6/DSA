n = int(input())
s = input()

result = 'Anton'
anton = s.count('A')
danik = s.count('D')
if anton < danik:
    result = 'Danik'
elif anton == danik:
    result = 'Friendship'
    
print(result)