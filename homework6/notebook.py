from tabulate import tabulate
import time
import json

headers1 = ["ID", "Text", "Created", "Updated"]
table_type = "rounded_grid"

def save_notes(notes, next_id=None):
    data = {"notes": notes, "next_id": next_id}
    with open ("notes.json", "w") as file:
        json.dump(data, file, indent=4)
        
def find_note_by_id(notes, note_id):
    for n in notes:
        if n["id"] == note_id:
            return n
    return None 
        
def breaker():
    print ("----------------")
    
def shorten_text (text, length=10):
    if len(text) > length:
        return text[:length-3] + "..." + text[len(text)-5]
    else:
        return text

def show_menu():
    breaker()
    print ("CHOOSE OPTION")
    print ("1: SHOW ALL NOTES")
    print ("2: SHOW NOTE DETAILS")
    print ("3: CREATE NOTE")
    print ("4: UPDATE NOTE")
    print ("5: DELETE NOTE")
    print ("Q: QUIT THE APPLICATION")
    print ("M: SHOW MENU AGAIN")
    breaker()

def show_all_notes(notes):
    if notes:
        table = [
            [
                note ["id"],
                shorten_text (note["text"]),
                note ["created"],
                note["updated"] if note["updated"] else "---"          
            ]
            for note in notes
        ]
        print (tabulate(
            table,
            headers = headers1,
            tablefmt = table_type
        ))
    else:
        print ("No notes found")
        
def show_note_details(notes):
    note_id = int(input("Enter note ID: "))
    note = find_note_by_id(notes, note_id)  
    if note:
        print (f"\nID: {note['id']}")
        print (f"Text: {note['text']}")
        print (f"Created: {note['created']}")
        print (f"Updated: {note['updated'] if note['updated'] else '---'}")
        print ("")
    else:
        print ("Note not found")

def create_note (notes, next_id):
    text = input ("Enter note's text: ")
    created = time.strftime("%Y-%m-%d %H:%M:%S")
    notes.append ({"id": next_id, "text": text, "created": created, "updated": None})
    print ("Note added")
    next_id += 1
    save_notes(notes, next_id)
    return next_id 
    
def update_note (notes):
    note_id = int (input ("Enter note ID to update: "))
    note = find_note_by_id(notes, note_id)
    if note:
        new_text = input ("Enter new text: ")
        note ["text"] = new_text
        note ["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
        print ("Note updated")
        save_notes(notes)
    else:
        print ("Note not found")

def delete_note (notes):
    note_id = int (input ("Enter note ID to delete: "))
    note = find_note_by_id(notes, note_id)
    try:
        if note:
            notes.remove(note)
            print("Note deleted.")
            save_notes(notes)
            print("Note deleted")
            return notes
        else:
            print("Note not found.")
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        
        


def save_notes(notes, next_id=None):
    data = {"notes": notes, "next_id": next_id} if next_id is not None else {"notes": notes}
    with open("notes.json", "w") as file:
        json.dump(data, file, indent=4)
        
        
def load_notes():
    try:
        with open("notes.json", "r") as file:
            data = json.load(file)
            notes = data.get("notes", [])
            next_id = data.get("next_id", 1)
            return notes, next_id
    except FileNotFoundError:
        return [], 1 

def main():
    notes, next_id = load_notes() 
    show_menu()
    while True:
        choice = input("Choice: ").strip().upper()
        if choice == "1":
            show_all_notes(notes)
        elif choice == "2":
            show_note_details(notes)
        elif choice == "3":
            create_note(notes, next_id)
            next_id += 1  
        elif choice == "4":
            update_note(notes)
        elif choice == "5":
            notes = delete_note(notes)
        elif choice == "Q":
            print("QUIT!")
            break
        elif choice == "M":
            show_menu()
        else:
            print("Invalid, try again")


if __name__ == "__main__":
    main()