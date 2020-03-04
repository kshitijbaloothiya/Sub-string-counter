def count_substring(string, sub_string):
    le1 = len(string)
    le2 = len(sub_string)
    count=0
    for i in range(0,le1):
        x=string.find(sub_string,i,(le2+i))
        if x!=-1:
            count=count+1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
print(len(sub_string))