# Q1: geometric progression = a*(r**n)
def geometric_sum(n,a,r):
    geo_sum = 0
    for i in range(n):
        geo_sum += a*(r**i)
    return geo_sum

#a = geometric_sum(4,2,3)
#print(a)

# Q2:ATM Machine
def withdraw_cash(available_bills, amount):
    available_bills.sort(reverse=True)
    result = []
    for bill in available_bills:
        if amount>=bill:
            count = amount // bill
            if count == 1:
                print(f"{count} money note of {bill}")
            else: 
                print(f"{count} money notes of {bill}")
            amount = amount - count*bill
    
    if amount>0:
        return "Amount cannot be withdrawn using the current available money notes."

#available_bills = [50, 100, 200, 500]
#print(withdraw_cash(available_bills, 3350))

# Q3: Fibonacci sequence Fn-1 + Fn-2
# 0, 1, 1, 2, 3, 5
def F_sum(n,m):
    a,b=0,1
    terms=[]
    for i in range(m+1): # need to include term m
        if i>n:
            terms.append(a)
        a,b = b, a+b

    expression = "+".join(map(str,terms))
    result = sum(terms)
    print(f"{expression}={result}")
#F_sum(2,5)

# Q4: Most frequent word
def most_frequent(txt):
    words = txt.split(" ")
    word_dict = {}
    max_count = 0
    max_list = []
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for count in word_dict.values():
        if count >max_count:
            max_count= count
    for word, count in word_dict.items():
        if count == max_count:
            max_list.append(word)
    return max_list

#print(most_frequent("I want to know how to achieve the things I want"))

# Q5: BinaryTree
class BinaryTree:
    def __init__(self,value = 0,left = None,right=None):
        self.value = value
        self.left = left
        self.right = right
def getMaxDepth(root):
    if root is None:
        return 0
    else:
        depth_left = getMaxDepth(root.left)
        depth_right = getMaxDepth(root.right)
        return max(depth_left,depth_right)+1
    
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
print(getMaxDepth(root))