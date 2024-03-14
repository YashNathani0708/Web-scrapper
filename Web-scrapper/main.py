import requests
from bs4 import BeautifulSoup
import sys


def display_latest_deals():
    # Function to fetch and display the latest deals from RedFlagDeals forum

    # Sending a GET request to the RedFlagDeals forum page
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/2/")
    response.raise_for_status()  # Checking if the request was successful

    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Initializing deal count
    deal_count = 0

    # Extracting and displaying the deals
    for listing in soup.select("li.row.topic"):
        try:
            # Extracting deal data

            # Getting store name
            store_element = listing.select_one('.topictitle_retailer')
            store = store_element.get_text(strip=True) if store_element else "N/A"

            # Getting item name
            item_element = listing.select_one('.topic_title_link')
            item = item_element.get_text(strip=True) if item_element else "N/A"

            # Getting number of votes
            votes_element = listing.select_one('.total_count_selector')
            votes = votes_element.get_text(strip=True) if votes_element else "N/A"

            # Getting username
            username_element = listing.select_one('.thread_meta_author')
            username = username_element.get_text(strip=True) if username_element else "N/A"

            # Getting timestamp
            timestamp_element = listing.select_one('.first-post-time')
            timestamp = timestamp_element.get_text(strip=True) if timestamp_element else "N/A"

            # Getting category
            category_element = listing.select_one('.thread_category a')
            category = category_element.get_text(strip=True) if category_element else "N/A"

            # Getting number of replies
            replies_element = listing.select_one('.posts')
            replies = replies_element.get_text(strip=True) if replies_element else "N/A"

            # Getting number of views
            views_element = listing.select_one('.views')
            views = views_element.get_text(strip=True) if views_element else "N/A"

            # Getting deal URL
            url_element = listing.select_one('.topic_title_link')  # Assuming '.href' is the correct selector
            url = url_element.get('href') if url_element else "N/A"

            deal_count += 1

            # Printing deal information
            print()
            print(f"Store: {store}")
            print(f"Item: {item}")
            print(f"Votes: {votes}")
            print(f"Username: {username}")
            print(f"Timestamp: {timestamp}")
            print(f"Category: {category}")
            print(f"Replies: {replies}")
            print(f"Views: {views}")
            print(f"URL: https://forums.redflagdeals.com/{url}")
            print()
            print("---------------------------------------------------------------------------------------")
        except Exception as e:
            # Handling exceptions
            print(f"An error occurred while extracting deal information: {e}")

    # Printing total number of deals found
    print(f"Total number of deals found: {deal_count}")


def analyze_deals_by_category():
    # Function to analyze deals by category on RedFlagDeals

    # Sending a GET request to the RedFlagDeals website
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/2/")
    response.raise_for_status()  # Checking if the request was successful

    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Dictionary to store categories and corresponding deal counts
    categories = {}

    # Extracting categories and corresponding deal counts
    for listing in soup.select("li.row.topic"):
        try:
            # Extracting category data
            category_element = listing.select_one('.thread_category a')
            category = category_element.get_text(strip=True) if category_element else "N/A"

            # Increment deal count for the category
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1
        except Exception as e:
            # Handling exceptions
            print(f"An error occurred while extracting deal information: {e}")

    # Printing the categories and corresponding deal counts
    print("Deals by Category:")
    print()
    for category, count in categories.items():
        print(f"{category}: {count}")

    print("-------------------------")


def find_top_stores():
    # Function to find and display the top stores based on deal count

    # Prompting the user to input the desired number of top stores to display
    num_top_stores = int(input("Enter the number of top stores to display: "))
    print()

    # Sending a GET request to the RedFlagDeals website
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/2/")
    response.raise_for_status()  # Checking if the request was successful

    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Dictionary to store stores and corresponding deal counts
    stores = {}

    # Extracting stores and corresponding deal counts
    for listing in soup.select("li.row.topic"):
        try:
            # Extracting store data
            store_element = listing.select_one('.topictitle_retailer')
            store = store_element.get_text(strip=True) if store_element else "N/A"

            # Increment deal count for the store
            if store in stores:
                stores[store] += 1
            else:
                stores[store] = 1
        except Exception as e:
            # Handling exceptions
            print(f"An error occurred while extracting deal information: {e}")

    # Sorting stores based on deal count in descending order
    sorted_stores = sorted(stores.items(), key=lambda x: x[1], reverse=True)

    # Printing the top stores based on the number of deals associated with each store
    print("Top Stores:")
    for store, count in sorted_stores[:num_top_stores]:
        print(f"           {store}: {count} deals")

    print("-------------------------------------")


def log_deal_information():
    # Function to extract and log deal information

    # Sending a GET request to the RedFlagDeals website
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/2/")
    response.raise_for_status()  # Checking if the request was successful

    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Dictionary to store categories and their corresponding elements
    categories = {}

    # Extracting categories and storing them with their elements
    for listing in soup.select("li.row.topic"):
        try:
            category_element = listing.select_one('.thread_category a')
            category = category_element.get_text(strip=True) if category_element else "N/A"
            if category not in categories:
                categories[category] = [listing]  # Initialize list with this listing
            else:
                categories[category].append(listing)  # Append listing to existing category key
        except Exception as e:
            # Handling exceptions
            print(f"An error occurred while extracting deal information: {e}")

    # Displaying categories to the user
    print("\nList of categories:")
    category_list = list(categories.keys())  # Converting category keys to a list
    for i, category in enumerate(category_list, 1):
        print(f"{i}. {category}")

    # Prompting the user for category choice
    try:
        choice = int(input("Enter the number corresponding to the category: ")) - 1
        selected_category = category_list[choice]
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        return

    # Extracting and logging URLs from the selected category
    with open('log.txt', 'a') as file:
        x = 0
        for listing in categories[selected_category]:
            try:
                url_element = listing.select_one('a.topic_title_link')  # Assuming this is the correct selector for URLs
                url = url_element['href'] if url_element and url_element.has_attr('href') else "N/A"
                if x == 0:
                    file.write('\n Links of ' + selected_category + ' deals are listed below:\n')
                file.write("https://forums.redflagdeals.com/" + url + '\n')
                x += 1
            except Exception as e:
                # Handling exceptions
                print(f"An error occurred while extracting URLs: {e}")

        print("All the links have been logged successfully.")
        print()


def exit_program():
    print("Exiting the program. Goodbye!")
    sys.exit(0)


def main_menu():
    print("****** Web Scraping Adventure ******")
    print("1. Display Latest Deals")
    print("2. Analyze Deals by Category")
    print("3. Find Top Stores")
    print("4. Log Deal Information")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice


if __name__ == "__main__":
    while True:
        user_choice = main_menu()
        if user_choice == '1':
            display_latest_deals()
        elif user_choice == '2':
            analyze_deals_by_category()
        elif user_choice == '3':
            find_top_stores()
        elif user_choice == '4':
            log_deal_information()
        elif user_choice == '5':
            exit_program()
            break
        else:
            print("Invalid choice, please try again.")
