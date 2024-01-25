def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "navjot" ,
        "student_id" : 10310971 ,
        "pizza_toppings" : ["PEPPERS","PEPPERONI","ONIONS"],
        "movies" : [
         {"title": "half girlfreind", "titanic": "conjuring"},
         {"title": "The Godfather", "fiction": "There will be blood"},
        ]
    }
         


    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "The beekeeper", "Poor things": "Lift"}
    about_me["movies"].append(new_movie) 

    print_student_name_and_id(about_me)
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name =about_me["navjot"]
    first_name = full_name.split()[0]
    student_id = about_me["10310971"] 

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me ["pizza toppings"].extend(toppings)
    about_me ["pizza toppings"].sort()
    about_me ["pizza_toppings"] = [topping.lower()  topping about_me ['pizza_toppings']]

    add_toppings = ("red peppers", "mushrooms")

    main()


    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("my favourite pizza toppings :")
    about_me ["pizza_toppings"]


    print(f"- {topping}")


    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()