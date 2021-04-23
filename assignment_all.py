# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def first_and_last_two_word(name):
    print(name[:2]+name[-2:])
def get_input():
    name=input("enter the word  ")
    try:
        
        
        if len(name)>=2:
            first_and_last_two_word(name)
        else:
            print("empty string")
            get_input()
    except Exception as e:
        print(e)
        get_input()
    
   
get_input()
    

# 2. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
value=input("enter the sentence...: ")
value1=value.find('not')

value2=value.find('poor')
if value2 >0 and value2>0:
    value=value.replace(value[value1:value2+4],'good')
    print(value)
else:
    print(value)

# 3. Write a Python program to get the largest number from a list.



numbers=int(input("enter number of elements in list : "))
def largeNumber(numbers):
    number_list=[]
    for i in range(1,numbers+1):
        elements=int(input("enter elements: "))
        number_list.append(elements)
    print(f"largest number is :{max(number_list)}")

largeNumber(numbers)
# or
numbers=int(input("enter number of elements in list : "))
def largeNumber(numbers):
    number_list=[]
    for i in range(1,numbers+1):
        elements=int(input("enter elements: "))
        number_list.append(elements)
    biggest=number_list[0]
    for i in number_list:
        if i>biggest:
            biggest=i
        
    return biggest

print(f"largest number is :{largeNumber(numbers)}")

# 4. Write a Python program to remove duplicates from a list.

def remove_duplicates(duplicates_list):
    result=[]
    for i in duplicates_list:
        if i not in result:
            result.append(i)
    return result

duplicates_list=[1,4,5,6,7,5,7,9]
print(remove_duplicates(duplicates_list))

# or 
def remove_duplicates(duplicates_list):
    unique=set(duplicates_list)
    result=list(unique)
    return result
print(remove_duplicates(duplicates_list))

# 5. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_member(list1,list2):
    boolan_answer=False

    for i in list1:
        for j in list2:
            if i==j:
                boolan_answer=True
            
    return boolan_answer   

lis1=[1,2,3,4,5]
lis2=[5,6,7,8,9]

print(common_member(lis1, lis2))

# 6. Write a Python script to sort (ascending and descending) a dictionary by value

def dictionairy():
   
    dic ={}    
    dic[2] = 56       
    dic[1] = 2 
    dic[5] = 12 
    dic[4] = 24
    dic[6] = 18      
    dic[3] = 23
    for i in sorted (dic.values(),reverse=True) :
        print(i)
dictionairy()

# 7. Write a Python script to check whether a given key already exists in a dictionary.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "name" in thisdict.keys():
    print("exist keys")
else:
    print("not exist keys")

# 8. Write a Python program to sort a dictionary by key.
def dictionairy():
       
    dic ={}    
    dic[2] = 56       
    dic[1] = 2 
    dic[5] = 12 
    dic[4] = 24
    dic[6] = 18      
    dic[3] = 23
    for i in sorted (dic.keys(),reverse=True) :
        print(i)
dictionairy()