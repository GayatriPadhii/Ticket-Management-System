from tkinter import *
from tkinter import messagebox
import backend
import ticket_generator

class MovieApp:
    def __init__(self, root):
        self.current_user = None
        self.root = root
        self.root.title("🍿 Movie Ticket Booking System 🎟️")
        self.root.geometry("1350x850+0+0")
        self.root.config(bg="#FFF5F7")

        backend.create_tables()
        self.selected = None

        self.vars = {name: StringVar() for name in
                     ["Movie_ID", "Movie_Name", "Release_Date", "Director", "Cast", "Budget", "Duration", "Rating"]}

        self.create_widgets()

    def create_widgets(self):
        # Movie list frame
        list_frame = Frame(self.root, bg="#FFF5F7")
        list_frame.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.movie_list = Listbox(list_frame, width=120, height=12, bg="#FFE8E8", fg="black",
                                  font=('Comic Sans MS', 12), bd=3, relief=GROOVE, yscrollcommand=scrollbar.set)
        self.movie_list.pack(side=LEFT, fill=BOTH)
        self.movie_list.bind("<<ListboxSelect>>", self.on_select)

        scrollbar.config(command=self.movie_list.yview)

        # Labels and Entries
        labels = ["🎬 Movie ID", "🎞️ Movie Name", "📅 Release Date", "🎬 Director",
                  "👥 Cast", "💰 Budget", "⏱️ Duration", "⭐ Rating"]

        field_keys = ["Movie_ID", "Movie_Name", "Release_Date", "Director", "Cast", "Budget", "Duration", "Rating"]

        for i, (label, key) in enumerate(zip(labels, field_keys)):
            Label(self.root, text=label + ":", font=('Comic Sans MS', 13, 'bold'),
                  fg="#D6336C", bg="#FFF5F7").grid(row=i + 1, column=0, sticky=E, padx=10, pady=3)

            Entry(self.root, textvariable=self.vars[key], font=('Comic Sans MS', 12),
                  width=40, bg="#FFFCF9", bd=2, relief=RIDGE).grid(row=i + 1, column=1, sticky=W, padx=5, pady=3)

        # Buttons Frame (after entries)
        btn_frame = Frame(self.root, bg="#FFF5F7")
        btn_frame.grid(row=10, column=0, columnspan=4, pady=30)

        buttons = [
            ("➕ Add", self.add_movie),
            ("📜 Display", self.display_movies),
            ("✏️ Update", self.update_movie),
            ("❌ Delete", self.delete_movie),
            ("🔍 Search", self.search_movie),
            ("🧹 Clear", self.clear_fields),
            ("🚪 Exit", self.exit_app),
            ("🎟️ Book Ticket", self.book_selected_movie)
        ]

        for i, (text, cmd) in enumerate(buttons):
            Button(btn_frame, text=text, width=14, font=('Comic Sans MS', 11, 'bold'),
                   bg="#FFB6C1", fg="black", relief=RAISED, bd=3, command=cmd)\
                .grid(row=0, column=i, padx=5, pady=5)

    def add_movie(self):
        data = [self.vars[key].get() for key in self.vars]
        if data[0]:
            backend.add_movie(*data)
            self.display_movies()
            self.clear_fields()

    def display_movies(self):
        self.movie_list.delete(0, END)
        for row in backend.view_movies():
            self.movie_list.insert(END, row)

    def on_select(self, event):
        try:
            index = self.movie_list.curselection()[0]
            self.selected = self.movie_list.get(index)
            for i, key in enumerate(self.vars):
                self.vars[key].set(self.selected[i + 1])
        except:
            pass

    def delete_movie(self):
        if self.selected:
            backend.delete_movie(self.selected[0])
            self.display_movies()
            self.clear_fields()

    def update_movie(self):
        if self.selected:
            data = [self.vars[key].get() for key in self.vars]
            backend.update_movie(self.selected[0], *data)
            self.display_movies()
            self.clear_fields()

    def search_movie(self):
        self.movie_list.delete(0, END)
        data = [self.vars[key].get() for key in self.vars]
        for row in backend.search_movies(*data):
            self.movie_list.insert(END, row)

    def clear_fields(self):
        for var in self.vars.values():
            var.set("")

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to leave the movie magic? 🎬"):
            self.root.destroy()

    def book_selected_movie(self):
        if self.selected:
            seat_no = self.vars['Movie_ID'].get() + "_A1"
            backend.book_ticket(self.current_user or "guest", self.selected[2], seat_no)
            bookings = backend.get_user_bookings(self.current_user or "guest")
            ticket_id = bookings[-1][0]
            ticket_generator.generate_ticket(self.current_user or "guest", self.selected[2], seat_no, ticket_id)
            messagebox.showinfo("🍿 Ticket Booked!", f"Ticket ID: {ticket_id}\nEnjoy your movie! 🎥")

# Launcher
def launch_gui(username):
    root = Tk()
    app = MovieApp(root)
    app.current_user = username
    root.mainloop()

# Test run
if __name__ == "__main__":
    root = Tk()
    app = MovieApp(root)
    app.current_user = "guest"
    root.mainloop()
