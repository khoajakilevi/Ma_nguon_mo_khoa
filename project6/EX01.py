from pymongo import MongoClient
from datetime import datetime


#buoc 1: ket noi toi mongodb
client = MongoClient('mongodb://localhost:27017/')
client.drop_database('tiktok1')
db = client['tiktok1']# chon csdl tiktok

#buoc 2: tap cac collection
users_collection = db['users']
videos_collection = db['videos']

#b3 add data
users_data = [
    { 'user_id': 1, 'username': 'user1', 'full_name': 'Nguyen Van A', 'followers': 1500, 'following': 200 },
    { 'user_id': 2, 'username': 'user2', 'full_name': 'Tran Thi B', 'followers': 2000, 'following': 300 },
    { 'user_id': 3, 'username': 'user3', 'full_name': 'Le Van C', 'followers': 500, 'following': 100 }
]
users_collection.insert_many(users_data)
videos_data = [
    { 'video_id': 1, 'user_id': 1, 'title': 'Video 1', 'views': 10000, 'likes': 500, 'created_at': datetime(2024, 1, 1) },
    { 'video_id': 2, 'user_id': 2, 'title': 'Video 2', 'views': 20000, 'likes': 1500, 'created_at': datetime(2024, 1, 5) },
    { 'video_id': 3, 'user_id': 3, 'title': 'Video 3', 'views': 5000, 'likes': 200, 'created_at': datetime(2024, 1, 10) }
]
videos_collection.insert_many(videos_data)

#buoc5: truy van du lieu
#buoc 5.1:xem tat ca nguoi dung
print("tat ca nguoi dung: ")
for user in users_collection.find():
    print(user)

#buoc 5.2: tim video co nhieu nguoi xem nhat
print("video co nhieu luot xem nhat")
mosted_viewed_video = videos_collection.find().sort('view', -1).limit(1)
for video in mosted_viewed_video:
    print(video)
