from tabulate import tabulate

notes = []

def shorten_text(text, length=10):
    return text if len(text) <= length else text[:length-3] + "..." + text[len(text)-5:]

def show_menu():

    print("--------------------------")
    print("CHOOSE OPTION")
    print("1: SHOW ALL NOTES")
    print("2: SHOW NOTE DETAILS")
    print("3: CREATE NOTE")
    print("4: UPDATE NOTE")
    print("5: DELETE NOTE")
    print("Q: QUIT THE APPLICATION")
    print("M: SHOW MENU AGAIN")
    print("--------------------------")
    
def show_all_notes(notes):
   
    if notes:
        table = [[note["id"], shorten_text(note["text"])] for note in notes]
        print(tabulate(table, headers=["id", "text"], tablefmt="grid"))
    else:
        print("No notes found")

def show_note_details(notes, note_id):
    
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        print(f"ID: {note['id']}")
        print(f"Text: {note['text']}")
    else:
        print("Note not found")

def create_note(notes, text):
    new_id = max([note["id"] for note in notes], default=0) + 1
    notes.append({"id": new_id, "text": text})
    print("Note added")

def update_note(notes, note_id, new_text):
    
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        note["text"] = new_text
        print("Note updated")
    else:
        print("Note not found")

def delete_note(notes, note_id):
    notes[:] = [note for note in notes if note["id"] != note_id]
    print("Note deleted")

def main():

    show_menu()
    while True:
        choice = input("Choice: ").strip().upper()
        if choice == "1":
            show_all_notes(notes)
        elif choice == "2":
            note_id = int(input("Enter note ID: "))
            show_note_details(notes, note_id)
        elif choice == "3":
            text = input("Enter note text: ")
            create_note(notes, text)
        elif choice == "4":
            note_id = int(input("Enter note ID to update: "))
            new_text = input("Enter new text: ")
            update_note(notes, note_id, new_text)
        elif choice == "5":
            note_id = int(input("Enter note ID to delete: "))
            delete_note(notes, note_id)
        elif choice == "Q":
            print("QUIT!")
            break
        elif choice == "M":
            show_menu()
        else:
            print("Invalid, try again")
