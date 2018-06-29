from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from urllib.request import urlopen
from appmuseos.models import Museum
from appmuseos.models import Page_user
from appmuseos.models import Configuracion_user
from appmuseos.models import Coment
from django.template.loader import get_template
from django.template import Context 
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import sys
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from appmuseos.models import Time_like


import xml.etree.ElementTree as ET


#Zona de  la extraccion de datos a partir del fichero xml
SOURCE='https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full'

#direction es true hacia delante
def extract_museums(previous, next, direction, museums):
    num_museums=len(museums)
    ne=int(next)
    pre=int(previous)
    print(pre)
    print(direction)
    if direction =='True':
        print("hola")
        if (ne+5)<num_museums:
            list_museums=museums[ne:ne+5]
            ne=ne+5
        elif (ne+5)==num_museums:
            list_museums=museums[ne:ne+5]
            ne=ne+5
        else:
            list_museums=museums[ne:num_museums]
            ne=ne+5
        if pre==0 and ne==5:
            pre=0
        else:
            pre=pre+5
    else:
        print("hola false")
        if (pre-5)>0:
            list_museums=museums[pre-5:pre]
            pre=pre-5
        elif (pre-5)==0:
            list_museums=museums[0:pre]
            pre=0
            print(pre)
        else:
            list_museums=museums[0:pre]
            pre=0
        
        ne=ne-5
            
    return(str((pre)), str(ne), list_museums)
        
#funcion para comprobar que todos los usuarios tiene configurado el nombre de su pagina, por si no se habia creado ante o inicialiado. Se descargara la informacion de todos los usuarios e intentara acceder uno a uno a su page_user, en aquello que no existan y de error, procedera a crear el page_user con el parametro adecuado.         
def get_pagename():
    print("funcion")
    alluser=User.objects.all()
    for user in alluser:
        print(user)
        try:
            page=Page_user.objects.get(user=user)
            print(page.page)
        except ObjectDoesNotExist:
            print("exception")
            namepage="Página de "+ user.username
            newpage=Page_user(user=user, page=namepage)
            print(newpage.page)
            newpage.save()
            
    return Page_user.objects.all()    
            

#acces=True, solo muestro accesbles
def get_topfive(acces):
    print(acces)
    
    if acces:
        print("che")
        tool=Museum.objects.filter(accessibility=True)
        for m in tool:
            print (m.num_likes)
    else:
        tool=Museum.objects.all()
        
    tool=tool.order_by('num_likes')
    tool=tool.exclude(num_likes=0)
    print(tool)
    tool=tool[:5]
    print(tool)
    return tool
    
def parser_xml(req):
    xmlFile = urlopen(SOURCE)
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    Museum.objects.all().delete()
    for listMuseos in root.iter('contenido'):
        try:
            print("-----------------------------------------")
            for museo in listMuseos.findall('atributos'):
                try:
                    nombre = museo.find('atributo[@nombre="NOMBRE"]').text
                    print (nombre)
                except AttributeError:
                    print ("Campo nombre NO encontrado")
                    pass

                try:
                    descripcion = museo.find('atributo[@nombre="DESCRIPCION-ENTIDAD"]').text
                    print (descripcion)
                except AttributeError:
                    descripcion = " "
                    print ("Campo descripcion NO encontrado")
                    pass

                try:
                    descripcion += museo.find('atributo[@nombre="DESCRIPCION"]').text
                    print (descripcion)
                except AttributeError:
                    print ("Campo descripcion2 NO encontrado")
                    pass

                try:
                    horario = museo.find('atributo[@nombre="HORARIO"]').text
                    print (horario)
                except AttributeError:
                    print ("Campo horario NO encontrado")
                    pass

                try:
                    transporte = museo.find('atributo[@nombre="TRANSPORTE"]').text
                    print (transporte)
                except AttributeError:
                    print ("Campo transporte NO encontrado")
                    pass

                #accesibilidad = int(museo.find('atributo[@nombre="ACCESIBILIDAD"]').text,2)
                if museo.find('atributo[@nombre="ACCESIBILIDAD"]').text == "0":
                    accesibilidad = False
                else:
                    accesibilidad = True
                print (accesibilidad)

                try:
                    contentURL = museo.find('atributo[@nombre="CONTENT-URL"]').text
                    print (contentURL)
                except AttributeError:
                    print ("Campo contentURL NO encontrado")
                    pass


                localizacion = museo.find('atributo[@nombre="LOCALIZACION"]')
                try:
                    nombre_via = localizacion.find('atributo[@nombre="NOMBRE-VIA"]').text
                    print (nombre_via)
                except AttributeError:
                    print ("Campo nombre_via NO encontrado")
                    pass
                try:
                    clase_vial = localizacion.find('atributo[@nombre="CLASE-VIAL"]').text
                    #clase_vial = "(" + clase_vial + ")"
                    print (clase_vial)
                except AttributeError:
                    print ("Campo clase_vial NO encontrado")
                    pass
                try:
                    numero = localizacion.find('atributo[@nombre="NUM"]').text
                    #numero = "NUM " + numero
                    print (numero)
                except AttributeError:
                    print ("Campo numero NO encontrado")
                    pass
                try:
                    localidad = localizacion.find('atributo[@nombre="LOCALIDAD"]').text
                    print (localidad)
                except AttributeError:
                    print ("Campo localidad NO encontrado")
                    pass
                try:
                    cod_postal = localizacion.find('atributo[@nombre="CODIGO-POSTAL"]').text
                    print (cod_postal)
                except AttributeError:
                    print ("Campo cod_postal NO encontrado")
                    pass
                try:
                    barrio = localizacion.find('atributo[@nombre="BARRIO"]').text
                    print (barrio)
                except AttributeError:
                    print ("Campo barrio NO encontrado")
                    pass
                try:
                    distrito = localizacion.find('atributo[@nombre="DISTRITO"]').text
                    print (distrito)
                except AttributeError:
                    print ("Campo distrito NO encontrado")
                    pass


                datosContacto = museo.find('atributo[@nombre="DATOSCONTACTOS"]')
                try:
                    telefono = datosContacto.find('atributo[@nombre="TELEFONO"]').text
                    print (telefono)
                except AttributeError:
                    print ("Campo telefono NO encontrado")
                    pass
                email=''
                try:
                    email = datosContacto.find('atributo[@nombre="EMAIL"]').text
                    print (email)
                except AttributeError:
                    print ("Campo email NO encontrado")
                    pass

        except AttributeError:
            print("***Campo no encontrado para: " + nombre + "***")
            pass



        museo = Museum(name = nombre, description = descripcion, horary = horario, transport = transporte,
                      accessibility = accesibilidad, url = contentURL, address = clase_vial + ": " +nombre_via + ", Nº:"+
                      numero + "|| " + localidad +"("+ cod_postal +")", barrio = barrio, district = distrito,
                      number_phone = telefono, mail = email)
        print("!!!!!!!!!!!!!!!!!!!!!!!!! Antes de guardar Museo !!!!!!!!!!!!!!!!!!!!!!!!!")
        museo.save()
        print("!!!!!!!!!!!!!!!!!!!!!!!!! Despues de guardar Museo !!!!!!!!!!!!!!!!!!!!!!!!!")
        nombre = descripcion = horario = transporte = accesibilidad = contentURL = None
        nombre_via = clase_vial = numero = localidad = cod_postal = barrio = distrito = telefono = email = None

    return HttpResponseRedirect('/')



def main_json(request):
   museum=get_topfive(False)
   data=serializers.serialize('json',museum) 
    
   template=get_template("museum/json.html")
   comtext=Context({'data':data})
   return HttpResponse(template.render(comtext))
   
@csrf_exempt    
def main (request):
    print("AQUI")
    charge_museums=Museum.objects.all()
    if len(charge_museums)==0:
        template=get_template("museum/new.html")
        museums = Context({'authenticated':request.user.is_authenticated(),
                                    'name':  request.user.username,
                                    'pages': get_pagename(),
                                    'inicio':True})
        return HttpResponse(template.render(museums))
    else:
        template=get_template("museum/home.html")
        try:
            Accesibility = request.GET['Acces']
            if Accesibility=='True':    
                print("1")
                museums = Context({'authenticated':request.user.is_authenticated(),
                                    'name':  request.user.username,
                                    'pages': get_pagename(),
                                    'museums': get_topfive(True),
                                    'acces':'False',
                                    'inicio':True})
                answer= HttpResponse(template.render(museums))                        
                answer.set_cookie('acces', True, 3600) 
            else:
                print("2")
                museums = Context({'authenticated':request.user.is_authenticated(),
                                    'name':  request.user.username,
                                    'pages': get_pagename(),
                                    'museums': get_topfive(False),
                                    'acces':'True',
                                    'inicio':True})
                answer= HttpResponse(template.render(museums))                        
                answer.set_cookie('acces', False, 3600)                    
            return answer 
             
        except:
            print("error")
            pass
        
        
        if 'acces' in request.COOKIES:
            cookie=request.COOKIES
            Accesibility=cookie['acces']
            print("ESTE:"+ Accesibility)
            if Accesibility=='True':
                print("hooallalaa")
                museums=Context({'authenticated':request.user.is_authenticated(),
                                'name':  request.user.username,
                                'pages': get_pagename(),
                                'museums': get_topfive(True),
                                'acces':'False',
                                'inicio':True})
                answer= HttpResponse(template.render(museums))                                              
                return answer
                
        print("tttt")        
        museums = Context({'authenticated':request.user.is_authenticated(),
                            'name':  request.user.username,
                            'pages': get_pagename(),
                            'museums': get_topfive(False),
                            'acces':'True',
                            'inicio':True})
                            
        answer= HttpResponse(template.render(museums))                                              
        return answer
    
    
def list_museum_json(request):
    museums=Museum.objects.all()
    data=serializers.serialize('json',museums)
    
    template=get_template("museum/json.html")
    comtext=Context({'data':data})
    return HttpResponse(template.render(comtext))
    
    
def list_museum (request):
    #parser_xml()
    #if (len(Museum.objects.all())==0):
        
    districts=Museum.objects.values_list('district', flat=True).distinct()
    districts=list(districts)
    districts.insert(0,'Todos')
    print(districts)
    try:
        Selection= request.GET['distrito']
        print(Selection+"hola")
        if Selection != "Todos":
            museums=Museum.objects.filter(district=Selection)
        else:
            museums=Museum.objects.all()
        print(museums)
    except:
        museums=Museum.objects.all()
        
    if 'acces' in request.COOKIES:
        cookie=request.COOKIES
        accesibility=cookie['acces']
        print (accesibility)
        print("hay cookie")
        if accesibility=='True':
            print("hay accesiilidad")
            museums=museums.exclude(accessibility=False)
    
    template=get_template("museum/all_museum.html")
    print(request.user.is_authenticated())
    museums = Context({'authenticated':request.user.is_authenticated(),
                        'name':  request.user.username,
                        'pages': get_pagename(),
                        'museums': museums,
                        'options': districts,
                        'inicio':False})
    print("0")
    return HttpResponse(template.render(museums))
  
def information (request):
    print("about")
    about = Context({'authenticated':request.user.is_authenticated(),
                    'name':  request.user.username,
                    'pages': get_pagename(),
                    'inicio':False})
    template=get_template("museum/about.html")
    return HttpResponse(template.render(about))
@csrf_exempt     
def new_coment(request):
    museo=Museum.objects.get(id=request.POST['id'])
    coment= Coment(museum=museo, text=request.POST['comentario'])
    coment.save()
    return HttpResponseRedirect("/museo/"+request.POST['id'])
@csrf_exempt     
def museum (request, id_museum):
    template=get_template("museum/moreinfo.html")
    
    museum=Museum.objects.get(id=id_museum)
    print(museum)
    try:
        coments=Coment.objects.all()
    except ObjectDoesNotExist:
        coments=None
    for c in coments:
        print(c)
   
        
    info = Context({'authenticated':request.user.is_authenticated(),
                    'name':  request.user.username,
                    'pages': get_pagename(),
                    'museum': museum,
                    'coments':coments,
                    'inicio':False})
    return HttpResponse(template.render(info))
    
@csrf_exempt         
def user_page (request,name):

    try :
        print(name)
        user=User.objects.get(username=name)
        museums=Museum.objects.filter(user_likes= user) 
        
        if 'acces' in request.COOKIES:
            cookie=request.COOKIES
            Accesibility=cookie['acces']
            if Accesibility=='True':
                museums=museums.exclude(accessibility=False)  
                               
        template=get_template("museum/user.html")
            
        if request.method=='GET':
            print("get")
            pre, next, list_mu =extract_museums(0, 0, 'True', museums)    

        elif request.method=='POST':
            print("post")
            pre= request.POST['Previous']
            next= request.POST['Next']
            action= request.POST['Action']
            print(action)
            pre, next, list_mu =extract_museums(str(pre), str(next), action, museums)    
        else:
            return HttpResponseRedirect("/")
        print(pre)
        if (pre==str(0)):
            ifpre=False
            print("false")
        else:
            ifpre=True
            print("true")
            
        if (int(next)>=(len(museums))):
            ifnext=False
        else:
            ifnext=True
        if name==request.user.username:
            owner=True
        else:
            owner=False            
        museums = Context({'authenticated':request.user.is_authenticated(),
                            'name': request.user.username,
                            'pages': get_pagename(),
                            'pagina':Page_user.objects.get(user=user).page,
                            'museums': list_mu,
                            'likes':Time_like.objects.filter(user=user),
                            'ifpre':ifpre,
                            'ifnext':ifnext,
                            'previous':pre,
                            'next':next,
                            'owner':owner,
                            'inicio':False})
                            
    
    except ObjectDoesNotExist:
        print("bye")
        return HttpResponseNotFound("404:Page not found")
        
    return HttpResponse(template.render(museums))
    
    
def user_page_json(request, name):
    user=User.objects.get(username=name)
    museums_user=Museum.objects.filter(user_likes= user) 
    print(museums_user)
    data=serializers.serialize('json',museums_user)
    
    template=get_template("museum/json.html")
    comtext=Context({'data':data})
    return HttpResponse(template.render(comtext))
    
def style (request):
    try:
        print("try")
        user=request.user
        style=get_template("museum/style.css")
        print(user)
        conf_user=Configuracion_user.objects.get(user=user)
        print("conf")
        style_user = Context({'user' :conf_user})
        print("context")
        return HttpResponse(style.render(style_user), content_type='text/css')
    except:
        return HttpResponse(style.render(), content_type='text/css')

def pri (request):
    try:
        user=request.user
        pri=get_template("museum/print.css")
        conf_user=Configuracion_user.get(user=user)
        style_user = Context({'user' :conf_user})
        return HttpResponse(pri.render(style_user), content_type='text/css')
    except:
        return HttpResponse(pri.render(), content_type='text/css')
    
def formu (request):
    pri=get_template("museum/login.html")
    return HttpResponse(pri.render())
    
@csrf_exempt    
def mylog(request):
    print("Log")
    username = request.POST['user']
    password = request.POST['password']
    print(password)
    user = authenticate(username=username, password=password)
    
    print(user)
    if user is not None:
        print("if")
        login(request, user)
    return HttpResponseRedirect('/')
    
@csrf_exempt     
def like(request):
    if request.method == 'POST':
        print('like')
        museum_name = request.POST['Museum']
        print(museum_name)
        user_name = request.user.username
        user=User.objects.get(username=user_name)
        museum_like=Museum.objects.get(name=museum_name)
        try:
            tool=museum_like.user_likes.get(username=user_name)
            print('ya estaba')
            return HttpResponseRedirect('/museos')  
        except ObjectDoesNotExist:
            print('añado')      
            museum_like.user_likes.add(user)
            museum_like.num_likes=museum_like.num_likes+1
            museum_like.save()
            date=Time_like(museum=museum_like, user=user)
            date.save()
            return HttpResponseRedirect('/museos')

@csrf_exempt
def configuration(request):
    if request.method == 'POST':
        user=request.user
        option=request.POST['option']
        if option=='name':
            page= Page_user.objects.get(user=user)
            page.page=request.POST['new_name']
            page.save()
        else: 
            try:
                config=Configuracion_user.objects.get(user=user)
                config.size=request.POST['size_letter']
                config.color=request.POST['color']
                config.save()
            except ObjectDoesNotExist:
                config=Configuracion_user(user=user, size=request.POST['size_letter'], color=request.POST['color'])
                config.save()
    return HttpResponseRedirect('/'+user.username)
        
    


