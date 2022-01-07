# The Young Hackers Club has organized a forum on its website. The forum has the following structure: each post either starts a new topic, 
# or is a response to some previous post and belongs to the same topic.
# After several months of using their forum, young hackers were interested in the question - what topic is the most popular on their forum. Help them figure it out.
# The first line contains an integer N - the number of messages in the forum (1 <= N <= 1000). The following lines describe the messages in chronological order.
# The message description, which is the start of a new topic, consists of three lines. The first line contains the number 0. 
# The second line contains the name of the topic. The name does not exceed 30 characters. The third line contains the text of the message.
# Print the name of the topic to which the largest number of messages belongs. If there are several such topics, then output the first one in chronological order.

n = int(input())  # input topics' count
reply = [0] * n  # list of reply's count
topics = [''] * n  # list of topics
for i in range(n):
    num = int(input())  # input number for topic
    if num == 0:
        reply[i] = i
        topics[i] = input()  # input the topic's name
        input()  # input message
    else:
        reply[i] = reply[num - 1]
        input()
cntreplys = {}  # create dictionary where key is topic's number, value - repeat's count
for rep in reply:
    cntreplys[rep] = cntreplys.get(rep, 0) + 1  # increase repeat's count on 1
ans = []
for topic in cntreplys:
    ans.append((-cntreplys[topic], topic))
print(topics[min(ans)[1]])
