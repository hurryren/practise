from datasketch import MinHash
import time
start = time.clock()
f = open('01_follow_list_10w.dos.txt',encoding ='utf-8',mode = 'r')

lines = f.readlines()
length_of_f = len(lines)  # 数据的长度

for i in range(1):
    i = 1
    first_user = lines[i]
    a = first_user.split()
    user_ID = a[0] + '    '+'\n'
    hash_value = [user_ID]
    # 创建一个该用户文件存储该用户与其他用户的minhash值
    f_hash  = open('user_minhash/'+str(i) +'.txt',mode = 'w',encoding = 'utf-8')
   # f_hash.write(a[0] + '    '+'\n')  # 写入该用户的ID
    for j in range(length_of_f-1):
        if(i == j):
            continue
        else:
            second_user = lines[j]
            
            b = second_user.split()
            data1 = a[2].split(',')
            data2 = b[2].split(',')

            m1, m2 = MinHash(), MinHash()
            for d in data1:
                m1.update(d.encode('utf8'))
            for d in data2:
                m2.update(d.encode('utf8'))
            #print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))
            if(m1.jaccard(m2) <= 0.0078125):
                continue
            else:
                new_value = b[0] + '    ' +str(m1.jaccard(m2)) + '\n'
                hash_value.append(new_value)

    #f_hash.write(b[0] + '    ' +str(m1.jaccard(m2)) + '\n')
    for item in hash_value:
        f_hash.write(item)
    f_hash.close()
            
f.close()
end = time.clock()
print(end - start)

# 排序

""" 
first_line = f.readline()
second_line = f.readline()
a = first_line.split()
user = a[0]
sum_of_fans = a[1]
fans = a[2].split(',')
for fan in fans:
    print(fan)
#print(a[2])
print(fans[int(sum_of_fans)-1])
f.close() """
""" m1, m2 = MinHash(), MinHash()
for d in data1:
    m1.update(d.encode('utf8'))
for d in data2:
    m2.update(d.encode('utf8'))
print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

s1 = set(data1)
s2 = set(data2)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
print("Actual Jaccard for data1 and data2 is", actual_jaccard) """