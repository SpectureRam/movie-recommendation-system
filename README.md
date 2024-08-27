# Movie Recommendation System

This project is a **Movie Recommendation System** built using Python, Streamlit, and various machine learning techniques. The system recommends movies to users based on a selected movie title by analyzing movie titles, genres, and user ratings. The project utilizes data from the **MovieLens** dataset.

## Features

- **Interactive Web Interface**: Built with Streamlit for a user-friendly experience.
- **Movie Search**: Search for a movie by title to get personalized recommendations.
- **Similar Movie Recommendations**: Provides a list of movies similar to the one searched based on user ratings and movie content.

## How It Works

1. **Data Loading**: Downloads and loads the `movies.csv` and `ratings.csv` files from Google Drive if they are not already present.
2. **Movie Search**: The user inputs a movie title, which is cleaned and vectorized. The system then finds movies with similar titles.
3. **Recommendation Engine**: For the selected movie, the system identifies similar movies based on user ratings using collaborative filtering techniques.

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```

4. **Data Files**:
    The `movies.csv` and `ratings.csv` files are automatically downloaded from Google Drive using the `gdown` library if they do not already exist in the project directory.

## Usage

1. Run the application using `streamlit run app.py`.
2. Open your web browser and navigate to `http://localhost:8501`.
3. Enter a movie title in the text input box (e.g., "Toy Story").
4. View the list of recommended movies based on the selected movie.

## Dependencies

- Python 3.7+
- Streamlit (`streamlit`)
- Pandas (`pandas`)
- Scikit-learn (`scikit-learn`)
- gdown (`gdown`)
- NumPy (`numpy`)

## Example

Search for a movie like "Toy Story," and the system will display top recommendations based on similar user preferences and movie characteristics.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

---

Feel free to adjust the content according to your project's specifics!
