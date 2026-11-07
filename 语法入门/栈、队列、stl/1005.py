s = input().strip()
st = []
ok = True
for c in s:
    if c == 'a':
        st.append(c)
    else: # 'b'
        if st and st[-1] == 'a':
            st.pop()
        else:
            ok = False
            break
if ok and len(st) == 0:
    print("Good")
else:
    print("Bad")
