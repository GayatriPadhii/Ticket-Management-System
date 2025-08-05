# backend.py

from db_connection import connect_db

def create_tables():
    con = connect_db()
    cur = con.cursor()

    # Table for Movies
    cur.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Movie_ID TEXT,
            Movie_Name TEXT,
            Release_Date TEXT,
            Director TEXT,
            Cast TEXT,
            Budget TEXT,
            Duration TEXT,
            Rating TEXT
        )
    """)

    # Table for User Bookings
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            movie_name TEXT,
            seat_no TEXT,
            booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    con.commit()
    con.close()


# ---------------------------- Movie CRUD ----------------------------

def add_movie(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO movies (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()

def view_movies():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    con.close()
    return rows

def delete_movie(id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM movies WHERE id=?", (id,))
    con.commit()
    con.close()

def search_movies(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    con = connect_db()
    cur = con.cursor()

    # Dynamically build WHERE clause based on non-empty inputs
    conditions = []
    values = []

    if Movie_ID: conditions.append("Movie_ID=?"); values.append(Movie_ID)
    if Movie_Name: conditions.append("Movie_Name=?"); values.append(Movie_Name)
    if Release_Date: conditions.append("Release_Date=?"); values.append(Release_Date)
    if Director: conditions.append("Director=?"); values.append(Director)
    if Cast: conditions.append("Cast=?"); values.append(Cast)
    if Budget: conditions.append("Budget=?"); values.append(Budget)
    if Duration: conditions.append("Duration=?"); values.append(Duration)
    if Rating: conditions.append("Rating=?"); values.append(Rating)

    if conditions:
        query = "SELECT * FROM movies WHERE " + " OR ".join(conditions)
        cur.execute(query, values)
    else:
        cur.execute("SELECT * FROM movies")  # No filter, return all

    rows = cur.fetchall()
    con.close()
    return rows


def update_movie(id, Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        UPDATE movies SET
        Movie_ID=?, Movie_Name=?, Release_Date=?, Director=?, Cast=?, Budget=?, Duration=?, Rating=?
        WHERE id=?
    """, (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating, id))
    con.commit()
    con.close()


# ---------------------------- Booking Management ----------------------------

def book_ticket(username, movie_name, seat_no):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO bookings (username, movie_name, seat_no)
        VALUES (?, ?, ?)
    """, (username, movie_name, seat_no))
    con.commit()
    con.close()

def get_user_bookings(username):
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM bookings WHERE username=?", (username,))
    bookings = cur.fetchall()
    con.close()
    return bookings
