# Leetcode
Not only have leetcode questions

## Q1.
Question:
1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

Learnt:
1. pattern = r'^(\w)\1(\w)(?!\1)\2$';
   (\w) for receive a char, \1 for repeat and make groups, need to add (?!\1) if AABB need defferent things.
2. in a for loop, the start and end index won't change even you modify them in the loop itself.
3. index.sort(reverse=True)；
   Need to reverse before del it
4. re.match(pattern, (req_list[x] + req_list[x + 1] + req_list[x + 2] + req_list[x + 3])) is not None; import re and it is a boolean.
5. 扫过一次string之后还再扫一次就用counter跟temp；
   while True -> for扫 counter+= -> if counter大于temp就让temp相等 -> else自然而然counter没有增长就break
6. 三个字母连在一起就看几次删除，AABB就扫多几遍随5.思路.
7. 有个小窗口，三个或者两个空间的，“length-2or3”是遍历次数.
