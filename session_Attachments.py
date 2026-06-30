
import requests
import os
#url = "https://petstore.swagger.io/pet/{petId}/uploadImage"

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"

files = {"file" : open("F:\\pics\\images.jfif" , 'rb' )}
response = requests.post(url , files=files)

print(os.path.exists("F:\\pics\\images.jfif"))
print(response.text)
print(response.status_code)

#need to revise this section