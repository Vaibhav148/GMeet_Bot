

# def fun(a): 
#     r = len(a)  
#     c = len(a[0]) 

#     s = [[0 for k in range(c+1)] for l in range(r+1)] 
#     maxLen = 0
#     for i in range(1,r+1):
#             for j in range(1,c+1):
#                 if (a[i-1][j-1]) == 1:
#                     s[i][j]=min(s[i-1][j],s[i][j-1],s[i-1][j-1])+1
#                     maxLen = max(maxLen, s[i][j])
      
#     return maxLen
 

 

# r = int(input())
# c = int(input())
# a = []
# b = []
# for i in range(r):
#   a.append(list(map(int,input().split())))
# print(a)



# print(main(a)) 

# # This code is contributed by Soumen Ghosh 

# import datetime 
import datetime
from datetime import date

def nearest(items, pivot):
    want = datetime.timedelta(days=2)
    wanted = datetime.datetime(2020,11,18)


    for x in items:
        g = datetime.datetime.combine(date.today(),pivot)
        h = datetime.datetime.combine(date.today(), x)

        a = abs(g - h)

        if g<h:
            if want > a:
                want = a
                wanted = x







    return wanted.hour


# s = {}
# s[9] = "09:05"
# s[10] = "10:15"
# s[11] = "11:25"
# s[12] = "12:35"
# if p_day!=1:

#     s[14] = "14:05"
#     s[13] = "14:05"

# x = datetime(2020,)
# y = datetime.time(13,0,0)

s = {}
s[9] = datetime.time(9,5,0)
s[10] = datetime.time(10,15,0)
s[11] = datetime.time(11,25,0)
s[12] = datetime.time(12,35,0)
s[14] = datetime.time(14,5,0)
# now = datetime.datetime.now().time()
now = datetime.time(18,20,0)
print(type(now))
# y = datetime.time()
print(nearest(list(s.values()),now))

# x = datetime.datetime(2020,11,18,14,5,0)
# y = datetime.datetime(2020,11,18,13,5,0)
# print(x-y)
# print(type(datetime.datetime.combine(date.today(),now)))
# diff = abs(datetime.datetime.combine(date.today(),x) - datetime.datetime.combine(date.today(), g))

# print(diff)