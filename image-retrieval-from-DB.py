'''Note: This example assumes that you have a table named 
"images" in your SQLite database, with a column named "image" 
that contains binary data for the images and a column named "id" 
that contains unique IDs for each image.'''

import sqlite3

def retrieve_image(conn, image_id):
    cursor = conn.cursor()
    cursor.execute("SELECT image FROM images WHERE id=?", (image_id,))
    return cursor.fetchone()[0]

conn = sqlite3.connect("images.db")
image = retrieve_image(conn, 1)
with open("image.jpg", "wb") as f:
    f.write(image)
