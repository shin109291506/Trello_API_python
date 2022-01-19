# 模組
import requests
import json

# Trello API Key & Token
key = 'YOUR_KEY_HERE'
token = 'YOUR_TOKEN_HERE'

# type : list
board = "YOUR_BOARD_HERE"

# 各種方法，詳見Trello API文件

#取得板子資訊
def GetBoard():
    url_get_board = "https://api.trello.com/1/boards/" + board 
    Request = {
    "boards":"open",
    "board_fields":["id","name"],
    'key': key,
    'token': token
    }
    req = requests.request("GET", url_get_board, params=Request)
    board_lists = json.loads(req.text)
    print(board_lists)
    
# 取得板子全部清單
def GetList():
    url_get_list = "https://api.trello.com/1/boards/" + board + "/lists"
    Request = {
    "cards":"open",
    "card_fields":["id","name"],#,"name","coordinates","pos"],   #https://developer.atlassian.com/cloud/trello/guides/rest-api/object-definitions/#card-object
    "filter":"open",
    "fields":"name",
    "key":key,
    "token":token
    }
    req = requests.request("GET", url_get_list, params=Request)
    card_lists = json.loads(req.text)
    return card_lists
    #print(card_lists)

#增加清單(板子id, 清單名稱(type:str))
def AddList(board_id, name):
    url_add_list = 'https://api.trello.com/1/lists'
    query = {
    "name":name,
    "idBoard":board_id,
    "key":key,
    "token":token
    }
    response = requests.request("POST", url_add_list, params=query)   
    print(response.text)
    print("List：", name, "新增完成")
    
#增加卡片(清單id, 卡片名稱(type:str))
def AddCard(list_id, name):
    url_add_card = 'https://api.trello.com/1/cards'
    query = {
    "idList":list_id,
    "name":name,
    #"keepFromSource":"all",
    #"due":day,
    "idBoard":board,
    "key":key,
    "token":token
    }
    response = requests.request("POST", url_add_card, params=query)
    #print(response.text)
    print("Card：", name, "新增完成")

#改變卡片名稱(卡片id, 卡片名稱(type:str))
def UpdateCard(card_id, textt):
    url_update_card = "https://api.trello.com/1/cards/"+card
    query = {
    "id":card_id,
    "name":textt,
    "key":key,
    "token":token,
    }
    response = requests.request("PUT", url_update_card, params=query)
    #print(response.text)
    print("Card：",card_id,"更新為",textt)

#新增卡片評論(卡片id, 評論內容(type:str))
def AddComment(card, response):
    url_add_comment = "https://api.trello.com/1/cards/"+card+"/actions/comments"
    query = {
    "id":card,
    "key":key,
    "token":token,
    "text":response
    }
    response = requests.request("POST", url_add_comment, params=query)
    #print(response.text)
    
#新增卡片附件(卡片id, 附件連結(type:str))
def AddAttachment(card, response):
    url_add_attachment = "https://api.trello.com/1/cards/"+card+"/attachments"
    query = {
    "id":card,
    "key":key,
    "token":token,
    "url":response
    }
    response = requests.request("POST", url_add_attachment, params=query)
    #print(response.text)
