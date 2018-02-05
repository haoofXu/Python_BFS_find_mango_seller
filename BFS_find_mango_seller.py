# -*- coding: utf-8 -*-


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque



def person_is_seller(name):
    return name[-1] == 'm'  # 检查是否以 m 结尾

def search(name):
    search_queue = deque()  # 创建一个队列
    search_queue += graph[name]
    searched = []   # 检查已用于检查记录的人
    while search_queue:
        person = search_queue.popleft()  # 就取出第一个人
        if person not in searched:  # 没检查过时才检查
            if person_is_seller(person):  # 检查这个人是否是芒果销售商
                print person + " is a mango seller!"
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")