from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Post,User
import requests
# Create your views here.

# def index(request):
#     return render(request,'main/index.html')

class GetUsersData():
    def getDB(str,method):
        r = requests.get("http://jsonplaceholder.typicode.com/"+str)
        r_dir= r.json()

        for i in r_dir:
            method(i)

    def sUsers(usersData):
        user = User()
        user.id=usersData['id']
        user.name=usersData['name']
        user.username=usersData['username']
        user.email=usersData['email']
        user.street=usersData['address']['street']
        user.suite=usersData['address']['suite']
        user.city=usersData['address']['city']
        user.zipcode=usersData['address']['zipcode']
        user.lat=usersData['address']['geo']['lat']
        user.lng = usersData['address']['geo']['lng']
        user.phone=usersData['phone']
        user.website=usersData['website']
        user.compName=usersData['company']['name']
        user.compCatchPhrase=usersData['company']['catchPhrase']
        user.compBs=usersData['company']['bs']
        user.save()

    def sPost(postData):
        post=Post()
        post.userId=postData['userId']
        post.id=postData['id']
        post.title=postData['title']
        post.body=postData['body']
        post.save()

    def getUserPost(requests,**kwargs):
        GetUsersData.getDB('users',GetUsersData.sUsers)
        GetUsersData.getDB('posts',GetUsersData.sPost)
        return render(requests,'main/base.html')



class Prints():
    def printUser(requests):
        users=User.objects.all()
        return render(requests,'main/about.html',{'user':users})

    def printPost(requests):
        post = Post.objects.all()
        p=[]
        for i in post:
            teg={}
            teg['name']=User.objects.get(id=i.userId).name
            teg['title']=i.title
            teg['body']=i.body
            p.append(teg)



        return render(requests,'main/index.html',{'title':'База данных','p':p})





















# def filt(request):
#     r = requests.get("http://jsonplaceholder.typicode.com/posts")
#     r_dir = r.json()
#     POST = []
#
#     for i in r_dir:
#         SLOV = []
#         for j in i:
#             SLOV.append(i[j])
#         post = Post(useid=SLOV[0], id=SLOV[1], title=SLOV[2], body=SLOV[3])
#         post.save()
#
#     r = requests.get("http://jsonplaceholder.typicode.com/users")
#     r_dir = r.json()
#     for i in r_dir:
#         SLOV = []
#         COMP = []
#         ADDRESS = []
#         GEO = []
#         for j in i:
#             if 'address' in j:
#                 ADDRESS.append(i['id'])
#                 SLOV.append(i['id'])
#
#                 for k in i[j]:
#
#                     if 'geo' in k:
#                         GEO.append(i['id'])
#                         GEO.append(i[j][k]['lat'])
#                         GEO.append(i[j][k]['lng'])
#                         ADDRESS.append(i['id'])
#                         continue
#                     ADDRESS.append(i[j][k])
#
#                 addr = Address(iD=ADDRESS[0], street=ADDRESS[1], suite=ADDRESS[2], city=ADDRESS[3], zipcode=ADDRESS[4],
#                                geo=ADDRESS[5])
#                 geo = Geo(iD=GEO[0], lat=GEO[1], lng=GEO[2])
#                 addr.save()
#                 geo.save()
#
#             elif 'company' in j:
#                 COMP.append(i['id'])
#                 SLOV.append(i['id'])
#                 for k in i[j]:
#                     COMP.append(i[j][k])
#                 co = Company(iD=COMP[0], name=COMP[1], cathPhrase=COMP[2], bs=COMP[3])
#                 co.save()
#
#             else:
#                 SLOV.append(i[j])
#         us = User(id=SLOV[0], name=SLOV[1], username=SLOV[2], email=SLOV[3], address=SLOV[4], phone=SLOV[5],
#                   website=SLOV[6], company=SLOV[7])
#         us.save()
#
#
#     post=Post.objects.all()
#     for i in post:
#         nameS = User.objects.get(pk=i.useid).name
#         table=Tabls(id=i.id,name=nameS,title=i.title,body=i.body)
#         table.save()
#
#     p = Tabls.objects.all()
#     return render(request,'main/about.html',{'title':'База данных','p':p})
#
# def about(request):
#     r = requests.get("http://jsonplaceholder.typicode.com/posts")
#     r_dir = r.json()
#     POST=[]
#
#     for i in r_dir:
#         SLOV = []
#         for j in i:
#             SLOV.append(i[j])
#         post=Post(useid=SLOV[0],id=SLOV[1],title=SLOV[2],body=SLOV[3])
#         post.save()
#
#     # po=Post.objects.filter(user=)
#
#     return render(request,'main/about.html')
#
# def use(request):
#
#     r = requests.get("http://jsonplaceholder.typicode.com/users")
#     r_dir = r.json()
#     for i in r_dir:
#         SLOV = []
#         COMP = []
#         ADDRESS = []
#         GEO = []
#         for j in i:
#             if 'address' in j:
#                 ADDRESS.append(i['id'])
#                 SLOV.append(i['id'])
#
#                 for k in i[j]:
#
#                     if 'geo' in k:
#                         GEO.append(i['id'])
#                         GEO.append(i[j][k]['lat'])
#                         GEO.append(i[j][k]['lng'])
#                         ADDRESS.append(i['id'])
#                         continue
#                     ADDRESS.append(i[j][k])
#
#                 addr=Address(iD=ADDRESS[0],street=ADDRESS[1],suite=ADDRESS[2],city=ADDRESS[3],zipcode=ADDRESS[4],geo=ADDRESS[5])
#                 geo=Geo(iD=GEO[0],lat=GEO[1],lng=GEO[2])
#                 # addr.save()
#                 # geo.save()
#
#             elif 'company' in j:
#                 COMP.append(i['id'])
#                 SLOV.append(i['id'])
#                 for k in i[j]:
#                     COMP.append(i[j][k])
#                 co=Company(iD=COMP[0],name=COMP[1],cathPhrase=COMP[2],bs=COMP[3])
#                 # co.save()
#
#             else:
#                 SLOV.append(i[j])
#         us=User(id=SLOV[0],name=SLOV[1],username=SLOV[2],email=SLOV[3],address=SLOV[4],phone=SLOV[5],website=SLOV[6],company=SLOV[7])
#         us.save()
#     post=User.objects.all()
#     return render(request,'main/index.html',{'post':post})






