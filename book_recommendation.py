# Predefined book database
book_recommendations = {
    "children": {
        "fiction": ["Harry Potter Series by J.K. Rowling", "Charlotte's Web by E.B. White"],
        "non-fiction": ["National Geographic Kids by National Geographic Society", "Goodnight Stories for Rebel Girls by Elena Favilli"],
        "fantasy": ["The Chronicles of Narnia by C.S. Lewis", "Percy Jackson Series by Rick Riordan"],
        "comedy": ["Diary of a Wimpy Kid by Jeff Kinney", "Captain Underpants by Dav Pilkey", "Wayside School is Falling Down by Louis Sachar"],
        "drama": ["Wonder by R.J. Palacio", "Bridge to Terabithia by Katherine Paterson", "The Miraculous Journey of Edward Tulane by Kate DiCamillo"],
        "thriller": ["Goosebumps series by R.L. Stine", "The Mysterious Benedict Society by Trenton Lee Stewart", "Escape from Mr. Lemoncello's Library by Chris Grabenstein"],
    },
    "teen": {
        "fiction": ["The Fault in Our Stars by John Green", "To All the Boys I've Loved Before by Jenny Han"],
        "non-fiction": ["Becoming by Michelle Obama (Young Readers Edition)", "The 7 Habits of Highly Effective Teens by Sean Covey"],
        "fantasy": ["The Hunger Games by Suzanne Collins", "Divergent Series by Veronica Roth"],
        "comedy": ["The Absolutely True Diary of a Part-Time Indian by Sherman Alexie", "The Princess Diaries by Meg Cabot", "Spud by John van de Ruit"],
        "drama": ["The Perks of Being a Wallflower by Stephen Chbosky", "Speak by Laurie Halse Anderson", "If I Stay by Gayle Forman"],
        "thriller": ["One of Us Is Lying by Karen M. McManus", "We Were Liars by E. Lockhart", "Miss Peregrine's Home for Peculiar Children by Ransom Riggs"]
    },
    "adult": {
        "fiction": ["The Great Gatsby by F. Scott Fitzgerald", "Where the Crawdads Sing by Delia Owens"],
        "non-fiction": ["Sapiens by Yuval Noah Harari", "Educated by Tara Westover"],
        "fantasy": ["The Name of the Wind by Patrick Rothfuss", "A Game of Thrones by George R.R. Martin"],
        "comedy": ["Good Omens by Neil Gaiman and Terry Pratchett", "Bossypants by Tina Fey", "Catch-22 by Joseph Heller"],
        "drama": ["A Thousand Splendid Suns by Khaled Hosseini", "The Night Circus by Erin Morgenstern", "Little Fires Everywhere by Celeste Ng"],
        "thriller": ["The Girl with the Dragon Tattoo by Stieg Larsson", "Gone Girl by Gillian Flynn", "The Silent Patient by Alex Michaelides"]
    }
}

# Function to recommend books
def recommend_books():
    print("Welcome to the Book Recommendation System!")
    print("Please choose an age group:")
    print("1. Children\n2. Teen\n3. Adult")
    
    age_group_choice = input("Enter the number corresponding to your choice: ").strip()
    age_group_map = {"1": "children", "2": "teen", "3": "adult"}
    age_group = age_group_map.get(age_group_choice)
    
    if not age_group:
        print("Invalid choice. Please restart the program.")
        return
    
    print("\nAvailable genres:")
    print("1. Fiction\n2. Non-Fiction\n3. Fantasy\n4. Comedy\n5. Drama\n6. Thriller")
    
    genre_choice = input("Enter the number corresponding to your choice: ").strip()
    genre_map = {
        "1": "fiction", "2": "non-fiction", "3": "fantasy",
        "4": "comedy", "5": "drama", "6": "thriller"
    }
    genre = genre_map.get(genre_choice)
    
    if not genre:
        print("Invalid choice. Please restart the program.")
        return
    
    recommendations = book_recommendations.get(age_group, {}).get(genre, [])
    if recommendations:
        print("\nRecommended Books:")
        for book in recommendations:
            print(f"- {book}")
    else:
        print("\nSorry, no recommendations available for the selected criteria.")
    
    print("\nThank you for using the Book Recommendation System!")

# Run the program
if __name__ == "__main__":
    recommend_books()
