a = {2, 5, 6, 3, 9}
b = {9, 7, 5, 6, 7}
c = {1, 4, 5, 7, 6}
print(a.intersection(b).intersection(c))


a = {2, 7, 6, 3, 9}
b = {9, 4, 5, 6, 7}
c = {1, 4, 5, 7, 9}
print(a.difference(b).difference(c))


ar = (1, 1, 9, 7, 23)
br = (3, 1, 8, 9, 7)
cr = (4, 1, 5, 7, 8)
if br[1] == cr[1] == ar[1]:
    print(ar[1])
if br[2] == cr[2] == ar[2]:
    print(ar[2])
if br[3] == cr[3] == ar[3]:
    print(ar[3])
if br[4] == cr[4] == ar[4]:
    print(ar[4])
if br[0] == cr[0] == ar[0]:
    print(ar[0])
