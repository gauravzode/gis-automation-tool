import sqlite3

DB_NAME = "youtube.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()



def list_all_videos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("\nNo videos found.")
    else:
        print("\n" + "*" * 50)
        for vid in videos:
            print(f"{vid[0]}. {vid[1]} | Duration: {vid[2]}")
        print("*" * 50)

    conn.close()



def add_video():
    name = input("Enter video name: ")
    time = input("Enter video duration: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)",
        (name, time)
    )

    conn.commit()
    conn.close()

    print("✅ Video added successfully.")



def update_video():
    list_all_videos()
    try:
        vid = int(input("Enter video ID to update: "))
    except ValueError:
        print("Invalid input.")
        return

    name = input("Enter new video name: ")
    time = input("Enter new video duration: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (name, time, vid)
    )

    if cursor.rowcount == 0:
        print("Invalid video ID.")
    else:
        print("✅ Video updated successfully.")

    conn.commit()
    conn.close()



def delete_video():
    list_all_videos()
    try:
        vid = int(input("Enter video ID to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM videos WHERE id = ?", (vid,))

    if cursor.rowcount == 0:
        print("Invalid video ID.")
    else:
        print("✅ Video deleted successfully.")

    conn.commit()
    conn.close()



def main():
    init_db()

    while True:
        print("\nYouTube Manager (SQLite)")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                print("Exiting application.")
                break
            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
