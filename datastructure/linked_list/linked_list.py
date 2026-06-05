# 1. CLASS DEFINITION
# Changed to 'ListNode' (Capital L) to match standard convention and your usage below
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. DATA CREATION
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
headl1 = node1  # Represents number 321

node5 = ListNode(7)
node6 = ListNode(5)
node7 = ListNode(9)
node5.next = node6
node6.next = node7
headl2 = node5  # Represents number 957

# 3. THE FUNCTION
# Removed 'self' because this is just a normal function now
def addtwonumbers(l1, l2):
    # Convert l1 to integer
    num1 = 0
    multiplier = 1
    while l1 != None:
        num1 += l1.val * multiplier
        multiplier *= 10
        l1 = l1.next
        
    # Convert l2 to integer
    num2 = 0
    multi = 1
    while l2 != None:
        num2 += l2.val * multi
        multi *= 10
        l2 = l2.next
        
    total_sum = num1 + num2
    
    # EDGE CASE FIX: If sum is 0, return a node with 0 immediately
    if total_sum == 0:
        return ListNode(0)

    dummy_head = ListNode(0)
    current = dummy_head
        
    while total_sum > 0:
        digit = total_sum % 10          # Get last digit
        current.next = ListNode(digit)  # Create node (using Capital L)
        current = current.next          # Move pointer
        total_sum = total_sum // 10     # Remove last digit

    return dummy_head.next

# 4. EXECUTION & TRAVERSE (Printing)
# Call the function
result_head = addtwonumbers(headl1, headl2)

# Traverse and Print
print("Result List:", end=" ")
while result_head is not None:
    print(result_head.val, end=" -> ")
    result_head = result_head.next
print("None")