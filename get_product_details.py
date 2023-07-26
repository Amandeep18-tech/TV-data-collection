from make_csv_tv_data import make_csv
import traceback
def get_details(product):
    title=get_title(product)
    brand=get_brand(product)
    mrp=get_mrp(product)
    price=get_price(product)
    num_reviews=get_num_reviews(product)
    num_ratings=get_num_ratings(product)
    avg_rating=get_avg_rating(product)
    product_url=get_product_url(product)
    image_url=get_image_url(product)
    
    make_csv(title,brand,price,mrp,num_reviews,num_ratings,avg_rating,product_url,image_url)

def get_title(product):
    product_name= None
    try:
        x=product.get('name',None)
        if x!=None and type(x)!=str:
            product_name=str(x)
        else:
            product_name=x
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return product_name

def get_brand(product):
    manufacturer_name=None
    try:
        x=product.get('manufacturer',None)
        if x!=None and type(x)!=str:
            manufacturer_name=str(x)
        else:
            manufacturer_name=x
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return manufacturer_name
    

def get_mrp(product):
    mrp=None
    try:
        x = product.get('mrp', {}).get('formattedValue', None)
        x=x.replace("₹", "").replace(",","")
        if x!=None and type(x)!=int:
            mrp=int(x)
        else:
            mrp=x
        
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return mrp


def get_price(product):
    price=None
    try:
        x = product.get('price', {}).get('formattedValue', None)
        x = x.replace("₹", "").replace(",","")
        if x!=None and type(x)!=int:
            price=int(x)
        else:
            price=x
        
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return price
   
def get_num_reviews(product):
    num_reviews= None
    try:
        x=product.get('numberOfReviews',None)
        if x!=None and type(x)!=int:
            num_reviews=int(x)
        else:
            num_reviews=x
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return num_reviews

def get_num_ratings(product):
    num_ratings= None
    try:
        x=product.get('numberOfRatings',None)
        if x!=None and type(x)!=int:
            num_ratings=int(x)
        else:
            num_ratings=x
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return num_ratings
    

def get_avg_rating(product):
    avg_rating= None
    try:
        x=product.get('averageRating',None)
        if x!=None and type(x)!=float:
            avg_rating=float(x)
        else:
            avg_rating=x
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return avg_rating

def get_product_url(product):
    product_url=None
    try:
        x=product.get('url',None)
        if x!=None:
            product_url="https://www.croma.com"+x
        
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return product_url

def get_image_url(product):
    image_url=None
    try:
        x=product.get('plpImage',None)
        if x!=None:
            image_url=x
        
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return image_url
    

def get_code(product):
    return product['code']