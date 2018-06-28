def extract_location(item):
    try:
        lane=item.find('atributos/atributo[@nombre="CLASE-VIAL"]').text
        street=item.find('atributos/atributo[@nombre="NOMBRE-VIA"]').text
        number=item.find('atributos/atributo[@nombre="NUM"]').text
        postal_code=item.find('atributos/atributo[@nombre="CODIGO-POSTAL"]').text
        locality=item.find('atributos/atributo[@nombre="LOCALIDAD"]').text
        
        address = lane + " : " + street + " | Num: " + number
        address += " | CP: " + postal_code + " | Localidad: " + locality 
        
        barrio = item.find('atributos/atributo[@nombre="BARRIO"]').text
        
        district=item.find('atributos/atributo[@nombre="DISTRITO"]').text
        
    except AtributeError:
        print("<<<Error en los datos de la Localizacion>>>")
        address, barrio, distric ='','', ''
        pass
        
    return address, barrio, district

def extract_contact(item):
    try:
        mail=item.find('atributos/atributo[@nombre="EMAIL"]').text
        telephone=item.find('atributos/atributo[@nombre="TELEFONO"]').text
    except:
        print("<<<Error en los datos de la Localizacion>>>")
        mail, telephone ='',''
        pass
        
    return mail, telephone


def extract_data(item):

    nombre, description, horary, transport = '', '', '', ''
    accessibility = False
    url, data_location, data_contacts = '','',''
    
    try:
        name=item.find('atributos/atributo[@nombre="NOMBRE"]').text
        print(name)
    except :
        print ("name_error")
        name=""
        pass
    try:
        description=item.find('atributos/atributo[@nombre="DESCRIPCION-ENTIDAD"]').text
        print(description)
    except :
        print ("description_error")
        description=""
        pass
    try:
       horary=item.find('atributos/atributo[@nombre="HORARIO"]').text
       print(horary)
    except :
        print ("horary_error")
        horary=""
        pass
    try:
        transport=item.find('atributos/atributo[@nombre="TRANSPORTE"]').text
        print(transport)
    except :
        print ("transport_error")
        transport=""
        pass
    try:
        if item.find('atributos/atributo[@nombre="ACCESIBILIDAD"]').text=="1":
            
            accessibility = True
        else: 
            accessibility = False
            
        print(accessibility)
    except :
        print ("accessibility_error")
        accessibility=False
        pass
    try:
        url=item.find('atributos/atributo[@nombre="CONTENT-URL"]').text
    except :
        print ("url_error")
        url=""
        pass
    try:
        lane=item.find('atributo[@nombre="CLASE-VIAL"]').text
        street=item.find('atributo[@nombre="NOMBRE-VIA"]').text
        number=item.find('atributo[@nombre="NUM"]').text
        postal_code=item.find('atributo[@nombre="CODIGO-POSTAL"]').text
        locality=item.find('atributo[@nombre="LOCALIDAD"]').text
        
        address = lane + " : " + street + " | Num: " + number
        address += " | CP: " + postal_code + " | Localidad: " + locality 
    except:
        print ("address_error")
        address=""
        pass
    try:
        barrio = item.find('/atributo[@nombre="BARRIO"]').text
    except:
        print ("barrio_error")
        barrio=""
        pass
    try :
        district=item.find('/atributo[@nombre="DISTRITO"]').text
    except:
        print ("district_error")
        district=""
        pass
    
    try:         
        data_contacts=item.find('atributos/atributo[@nombre="DATOSCONTACTOS"]').text
        mail, numbre_phone=extract_contact(data_contacts)
    except :
        print ("data_contacts_error")
        name=""
        pass
        
    try:
        museum = Museum(name=name, description=description, horary=horary, transport=transport,
        address=address, barrio=barrio, district=district, number_phone=number_phone,
        mail=mail,accessibility=accessibility, url=url)
        museum.save()
        print('<<<Museo Guardado>>>')
        
    except:
        print('<<<Error al guardar museo, es posible que aalgun dato este dañadoo>>>')
        pass

