from Trello_Action import *

List = GetList()

#從List提取card再提取card的id
for lists in List:
    for card in lists['cards']:
        print(card['id'])
