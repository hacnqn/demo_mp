import sys
import requests	
"""
1 Inicio su entorno python
2 ejecute script python demo_mp <id_vendedor> ej: python demo_mp 179571326
3 Recupere salida en ./
"""
def demo_mp(_param):
    _params= _param.split(",")
    file_out = open(r"demo-log.txt","w+")    
    for _id in _params:       
        response = requests.get('https://api.mercadolibre.com/sites/MLA/search?seller_id='+_id)
        data = response.json()
        items = data['results']    
        print ('procesando...')
        cant_items=len(items)
        index=0
        while index < cant_items:
            id=str(items[index]['id'])  
            title = str(items[index]['title'])
            category_id=str(items[index]['category_id'])
            response2 = requests.get('https://api.mercadolibre.com/categories/'+category_id)
            data2 = response2.json()
            category_name = str(data2['name'])
            str1 = _id +';'+id +';'+title+';'+category_id+';'+ category_name
            file_out.write('{}\n'.format(str1))       
            index+=1 
    print ('fin')
    file_out.close()
	
if __name__ == "__main__":
    id = sys.argv[1]
    demo_mp(id)