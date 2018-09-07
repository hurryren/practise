from datasketch import MinHash
import time
start = time.clock()
f = open('01_follow_list_10w.dos.txt',encoding ='utf-8',mode = 'r')

lines = f.readlines()
length_of_f = len(lines)  # 数据的长度


def xiaoming(lines,length_of_f,i):
    first_user = lines[i]
    a = first_user.split()
    user_ID = a[0] + '    '+'\n'
    print(a[1])
    hash_value = [0 for i in range(0,51)]   #该列表用于写入文件
    sort_value = [0 for i in range(0,51)]   #该列表用于放置更新中的值
    # 创建一个该用户文件存储该用户与其他用户的minhash值
    #f_hash  = open('user_minhash/'+a[0]+'.txt',mode = 'w',encoding = 'utf-8')
   # f_hash.write(a[0] + '    '+'\n')  # 写入该用户的ID
    for j in range(length_of_f-1):
        if(i == j):
            continue
        else:
            second_user = lines[j]
            
            b = second_user.split()
            data1 = a[2].split(',')
            data2 = b[2].split(',')

            #若果两列表相同个数为0或者一，舍去
            length_of_data1_and_data2 = len(data1) + len(data2)
            #去重
            both_data1_2 = list(set(data1+data2))
            
            if((length_of_data1_and_data2 - len(both_data1_2)) > 20):
                m1, m2 = MinHash(), MinHash()
                for d in data1:
                    m1.update(d.encode('utf8'))
                for d in data2:
                    m2.update(d.encode('utf8'))
                #print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))
                if(m1.jaccard(m2) <= 0.0078125):
                    continue
                else:
                    c = [b[0],m1.jaccard(m2)]
                    for m in range(49,-1,-1):
                        if (sort_value[m]==0):
                            sort_value[m] = c
                        else:
                            if(c[1] > sort_value[m][1]):
                                sort_value[m+1] = sort_value[m]
                                sort_value[m] = c
                            else:
                                break
            else:
                continue
                #new_value = b[0] + '    ' +str(m1.jaccard(m2)) + '\n'
                #hash_value.append(new_value)

    return sort_value
    #f_hash.write(b[0] + '    ' +str(m1.jaccard(m2)) + '\n')
    """ for item in sort_value:
        f_hash.write(str(item))
        f_hash.write('\n')
    f_hash.close() """



f_hash  = open('user_minhash/xiaoming'+'.txt',mode = 'w',encoding = 'utf-8')



for i in range(1):
    f_hash.write(lines[i].split()[0] + '          ')
    a = xiaoming(lines,length_of_f,i)
    for item in a:
        f_hash.write(str(item)+', ')  
    #f_hash.write('\n\n\n\n')     





f.close()
f_hash.close()
end = time.clock()
print(end - start)
