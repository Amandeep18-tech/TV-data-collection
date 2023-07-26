import csv
import textdistance
import statistics
csv_file_path = 'products.csv'

def get_title():
    with open(csv_file_path, mode='r', newline='') as csvfile:
        titles=[]
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Access details for each row using the field names (columns)
            title = row['Title']

            titles.append(title)
    
    return titles


def get_price__and_rating(jaro_winkler_values_greater_than_median):
    price_dict={}
    avg_rating_dict={}
    with open(csv_file_path, mode='r', newline='') as csvfile:
        
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Access details for each row using the field names (columns)
            price = row['Price']
            title = row['Title']
            average_rating = row['Average Rating Score']
            if title in jaro_winkler_values_greater_than_median:
                price_dict[title]=int(price)
                avg_rating_dict[title]=float(average_rating)
    return price_dict,avg_rating_dict

def get_jaro_winkler(user_tv_input):
    jaro_Winker_values = {} 
    titles=get_title()
    
    for title in titles:
        
        jaro_Winkler_distance =textdistance.jaro_winkler(user_tv_input.lower(), title.lower())
        jaro_Winker_values[title] = jaro_Winkler_distance
    return jaro_Winker_values


def get_median(sorted_list):
    return statistics.median(sorted_list)

def calculate_close_values_greater_than_median(levenshtein_values):
    sorted_pairs = sorted(levenshtein_values.items(), key=lambda x: x[1])

    # Extract the values from sorted key-value pairs
    sorted_values = [pair[1] for pair in sorted_pairs]

    # Step 2: Calculate the median
    median = get_median(sorted_values)
    print(median)

    # Step 3: Get all values greater than the median and convert to dictionary
    key_value_pairs_greater_than_median = {
        key: value for key, value in sorted_pairs if value > median
    }

    return key_value_pairs_greater_than_median


def get_best_match_with_user(jaro_winker_values_greater_than_median):
    top_3_elements = sorted(jaro_winker_values_greater_than_median.items(
    ), key=lambda item: item[1],reverse=True)[:3]
    print("Top 3 elements with the greatest values:")
    for key, value in top_3_elements:
        print(f"{key}")

def get_top_3_lowest_price(price_dict):
    top_3_lowest_prices = dict(sorted(price_dict.items(), key=lambda item: item[1])[:3])
    print("Top 3 Lowest Prices:")
    for title, price in top_3_lowest_prices.items():
        print(f"{title}: {price}")
        
def get_top_3_highest_rating(avg_rating_dict):
    top_3_highest_rating = dict(sorted(avg_rating_dict.items(), key=lambda item: item[1], reverse=True)[:3])
    print("Top 3 highest rating product")
    for title, rating in top_3_highest_rating.items():
        print(f"{title}: {rating}")

def main():
    while True:
        user_tv_input = input('Enter the TV you are searching for:')
        if user_tv_input == 'STOP':
            break

        jaro_winkler_values = get_jaro_winkler(user_tv_input)
    
        jaro_winkler_values_greater_than_median = calculate_close_values_greater_than_median(
            jaro_winkler_values)
        
        get_best_match_with_user(jaro_winkler_values_greater_than_median)
        price_dict,avg_rating_dict= get_price__and_rating(jaro_winkler_values_greater_than_median)
        get_top_3_lowest_price(price_dict)
        get_top_3_highest_rating(avg_rating_dict)
    

if __name__ == "__main__":
    main()

# Samsung 8 Series 163 cm (65 inch) 4K Ultra HD LED Tizen TV with Adaptive Sound
