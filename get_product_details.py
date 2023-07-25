from make_csv_tv_data import make_csv
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
    return product['name']

def get_brand(product):
    return product['manufacturer']

def get_mrp(product):
    return product['mrp']['formattedValue']

def get_price(product):
    return product['price']['formattedValue']

def get_num_reviews(product):
    return product['numberOfReviews']

def get_num_ratings(product):
    return product['numberOfRatings']

def get_avg_rating(product):
    return product['averageRating']

def get_product_url(product):
    return "https://www.croma.com"+product['url']

def get_image_url(product):
    return product['plpImage']

def get_code(product):
    return product['code']