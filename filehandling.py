# f = open("newfile.txt",'w')
# f.write("hello surbhi")
# f.close()


# f = open("newfile.txt",'a')
# f.write(" surbhi.txt")
# f.close()

# f = open("newfile.txt",'r')
# read = f.read()
# print(read)
# f.close()

# f = open("newfile.txt",'a')
# f.write("surbhi\n sona")
# f.close()

# f = open("newfile.txt",'w')
# # f.writelines("hello surbhi")
# f.writelines(['hello' ,' world',' welcome'])
# f.close()

# f = open ("newfile.txt",'r')
# read = f.readline()
# print(len(read))
# # print(type(read))
# f.close()

# f = open("newfile.dat",'wb')
# f.write(b" hello surbhi")
# f.close()

# f = open("newfile.dat",'rb')
# cona = f.read()
# print(cona)
# f.close()


# class Animal:
#     def dog(self,name):
#         print(name)
#     def cat(self):
#         print("juliya")
# object = Animal()
# object.dog("tommy")
# object.cat()


# class student:
#     school_name = "NSTI Dehradun"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(f"Student name is {self.name} and her age is {self.age}")

# o = student("Surbhi",40)
# o.get_details()

# i = student("Somya",18)
# i.get_details()

# j = student("Vikas",22)
# j.get_details()

            
# class Animal:
#     def __init__(self,name,age, ):
#         self.name = name
#         self.age = age
        

#     def dog(self):
#         return (self.name, self.age )    

#     def get_details(self):
#         print(f' his name is {self.name} and his age is {self.age}')

# object = Animal("Tan",4,)
# # print(object.dog("male"))    
# object.get_details()       


# class Human:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def Human(self):
#         return(self.name, self.age, self.gender)

#     def get_details(self):
#         print(f"her name is {self.name} her age is {self.age} and her gender is {self.gender}.")

# object = Human("Surbhi" , 22 ,"female")
# object.get_details()


# import requests
# response = requests.get("https://www.youtube.com/")
# print(response.headers)


# import requests
# from bs4 import BeautifulSoup

# def scrape_example():
#     url = 'https://www.youtube.com/'
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title = soup.title.get_text()
#         print(f"title of the page:{title}")
#     else:
#         print(f"failed to retrieve the page. status code:{response.status_code}")

# if __name__ == "__main__":
#     scrape_example()


import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# h3 = (soup.find("h3"))
# print(h3.a['title'])

# product_price = soup.find("div",class_ = "product_price")
# print(product_price)

product_price = soup.find_all(class_ = "price_color")
for price in product_price:
    print(price.text)