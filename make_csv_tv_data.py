import csv
def make_header():
    csv_file_path = 'products.csv'
    fields = ['Title', 'Brand', 'MRP', 'Price', 'Count of Ratings', 'Count of Reviews', 'Average Rating Score', 'Product URL', 'Image URL']
    with open(csv_file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
       
def make_csv(title, brand, mrp, price, count_of_ratings, count_of_reviews, average_rating_score, product_url, image_url):
    csv_file_path = 'products.csv'
    with open(csv_file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the data row to the CSV file
        writer.writerow([title, brand, mrp, price, count_of_ratings, count_of_reviews, average_rating_score, product_url, image_url])
    