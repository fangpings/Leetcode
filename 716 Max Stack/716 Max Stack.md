### 716 Max Stack

Design a max stack that supports push, pop, top, peekMax and popMax.

1. push(x) -- Push element x onto stack.
2. pop() -- Remove the element on top of the stack and return it.
3. top() -- Get the element on the top.
4. peekMax() -- Retrieve the maximum element in the stack.
5. popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

**Example 1:**

```
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
```

**Note:**

1. -1e7 <= x <= 1e7
2. Number of operations won't exceed 10000.
3. The last four operations won't be called when stack is empty.

### 想法

这道题怎么看也不应该是easy...

这里也用了一个很牛逼的技巧：两个stack

第一个stack就是普通的stack，第二个stack用于保存当前元素入栈的时候整个栈的最大值（这个只需要当前元素和入栈前第二个栈的栈顶元素比较就可以了），这样只有popMax不是O(1)了，popMax我们不断pop两个栈，直到两个栈的栈顶元素相同，这个时候我们再把之前pop出去的元素一个一个再加回来。。

这个还有改进的余地，我们把第二个栈换成heap，这样我们同样遇到了我们在218 skyline problem里面遇到的问题，那就是pop1的时候，2的位置无法维护，pop2的时候，1的位置无法维护。同样，我们利用lazy delete，我们再设置两个数据结构，一个记录在2中出栈的元素dict1，另一个记录在1中出栈的元素dict2，一旦我们在1中出栈，我们不动2，只是在dict2中标记一下，等我们需要2的最大元素（相当于栈顶），我们不断地popmax直到当前栈顶的元素不在dict2中了。同理，一旦我们在2中popmax，我们也只在dict1中标记而不动栈1。

上面这个方法是平均O(logN),其实还有真O(logN)的办法，那就是用红黑树了，但是红黑树也太复杂了，有空再去学吧。。