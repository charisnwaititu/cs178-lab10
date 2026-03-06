# name: Charis Waititu
# date: 03/05/2026
# description: Implementation of CRUD operations with DynamoDB — CS178 Lab 10
# proposed score: 0 (out of 5) -- if I don't change this, I agree to get 10 points.

import boto3

# boto3 uses the credentials configured via `aws configure` on EC2gu

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table("WeirdIceCreamFlavors")


def create_icecream():
    """
    Prompt user for a Movie Title.
    Add the movie to the database with the title and an empty Ratings list.
    """
    flavour = input("What is the Ice Cream flavour? ")
    calories = int(input("Calories: "))
    cream_type = input("Type: ")

    table.put_item(
        Item={
            "Flavour": flavour,
            "Calories": calories,
            "Type": cream_type
        }
    )

def print_icecream(cream):
    Flavour = cream.get("Flavour", "Unknown Flavour")
    Calories = cream.get("Calories", "Unknown")
    Type = cream.get("Type", "Unknown")

    print(f"  Flavour  : {Flavour}")
    print(f"  Calories : {Calories}")
    print(f"  Type     : {Type}") 

def print_all_icecream():
    """Scan the entire WeirdIceCreamFlavors table and print each item."""
    
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No Ice Cream found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} Ice Scream:\n")
    for cream in items:
        print_icecream(cream)

def update_icecream():
    try:
        title = input("What is the Ice Cream? ")
        calories = int(input("New calories: "))
        table.update_item(
            Key={"Flavour": title},
            UpdateExpression="SET Calories = :c",
            ExpressionAttributeValues={":c": calories}
        )
    except Exception:
        print("error in updating movie rating")



def delete_icecream():
    """
    Prompt user for an Ice Cream Flavour.
    Delete that item from the database.
    """
    title = input("What is the Ice Cream Flavour? ")
    table.delete_item(Key={"Flavour": title})

def query_icecream():
    title = input("What is the Ice cream flavour? ")

    response = table.get_item(Key={"Flavour": title})
    cream = response.get("Item")

    if not cream:
        print("ice cream not found")
        return

    print_icecream(cream)

def print_menu():
    print("----------------------------")
    print("Press C: to CREATE a new Ice Cream")
    print("Press R: to READ all Ice Cream")
    print("Press U: to UPDATE Ice Cream (change the calories)")
    print("Press D: to DELETE an Ice Cream Flavour")
    print("Press Q: to QUERY ")
    print("Press X: to EXIT application")
    print("----------------------------")

def main():
    input_char = ""
    while input_char.upper() != "X":
        print_menu()
        input_char = input("Choice: ")
        if input_char.upper() == "C":
            create_icecream()
        elif input_char.upper() == "R":
            print_all_icecream()
        elif input_char.upper() == "U":
            update_icecream()
        elif input_char.upper() == "D":
            delete_icecream()
        elif input_char.upper() == "Q":
            query_icecream()
        elif input_char.upper() == "X":
            print("exiting...")
        else:
            print("Not a valid option. Try again.")

main()
