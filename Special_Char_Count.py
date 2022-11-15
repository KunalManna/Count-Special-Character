#Count the Special charcter in the given string except space 
s=input("Enter the string:\n")        #aa a234Bc@@# Sad$%%  hsgv*
count=0
for i in s:
    if not ((i>='0' and i<='9') or (i>='A' and i<='Z') or (i>='a' and i<='z') or (i==' ')):
        count+=1
print(count)
