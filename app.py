from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data (genre and age group)
        genre = request.form.get('genre')
        age_group = request.form.get('age_group')

        # Get recommendations based on genre and age group
        books = get_book_recommendations(genre, age_group)
        
        # Return the recommendations to the template
        return render_template('index.html', books=books)

    # If GET request, just render the empty form
    return render_template('index.html', books=None)

def get_book_recommendations(genre, age_group):
    # Sample book recommendation logic (replace with actual logic)
    if genre == 'fiction' and age_group == 'children':
        return ['Harry Potter', 'Matilda', 'The Lion, the Witch and the Wardrobe']
    elif genre == 'fiction' and age_group == 'teen':
        return ['The Hunger Games', 'To Kill a Mockingbird', 'Divergent']
    elif genre == 'non-fiction' and age_group == 'adult':
        return ['Sapiens', 'Educated', 'Becoming']
    return []

if __name__ == "__main__":
    app.run(debug=True)
