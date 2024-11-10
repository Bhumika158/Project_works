import requests
import datetime as dt
TOKEN="xndwjknew324"
USERNAME="bhumika158"
GRAPH_ID= "coding-graph"
user_data={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# user_create= requests.post(url="https://pixe.la/v1/users",json=user_data)
# print(user_create.text)

graph_config={
    "id":GRAPH_ID,
    "name":"coding_tracker",
    "unit":"hours",
    "type":"float",
    "color":"sora"
}
headers={
    "X-USER-TOKEN":TOKEN
}

# graph_create= requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs",json=graph_config,headers=headers)
# print(graph_create.text)

date= dt.datetime.now().strftime("%Y%m%d")
pixel_data={
    "date":date,
    "quantity":input("How many hours did you studied today?")
}
post_pixel=requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}",json=pixel_data,headers=headers)
print(post_pixel.text)
# update_pixel_data={
#     "quantity":"2.0"
# }
# put_pixel=requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}",json=update_pixel_data,headers=headers)
# print(put_pixel.text)