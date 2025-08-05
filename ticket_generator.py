# ticket_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_ticket(username, movie_name, seat_no, ticket_id):
    filename = f"Ticket_{ticket_id}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "🎟️ Movie Ticket 🎟️")

    c.setFont("Helvetica", 14)
    c.drawString(100, height - 100, f"Ticket ID     : {ticket_id}")
    c.drawString(100, height - 130, f"User Name     : {username}")
    c.drawString(100, height - 160, f"Movie Name    : {movie_name}")
    c.drawString(100, height - 190, f"Seat Number   : {seat_no}")
    c.drawString(100, height - 220, f"Booking Status: Confirmed ✅")

    c.setFont("Helvetica-Oblique", 12)
    c.drawString(100, height - 270, "Thank you for booking with us! Enjoy the show! 🍿")

    c.save()

    # Optional: auto-open the ticket file (Windows only)
    try:
        os.startfile(filename)
    except AttributeError:
        pass  # For non-Windows OS, ignore
