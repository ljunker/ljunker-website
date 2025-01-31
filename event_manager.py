import json
import os
import sys
from pathlib import Path
import copy

common_events = [
    {
        "details": "Clubabend Ohmoor Squeezers",
        "location": "Wagrierweg 18, 22455 Hamburg"
    },
    {
        "details": "Clubabend der Elbe Beach Hoppers",
        "location": "Am Isfeld 19, 22589 Hamburg"
    }
]

def load_events(file_path):
    """Load events from a JSON file."""
    if not Path(file_path).exists():
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_events(events, file_path):
    """Save events to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4, ensure_ascii=False)
    print(f"Changes saved to {file_path} successfully!")

def list_events(events):
    """Display all events."""
    if not events:
        print("\nNo events found.")
        return False

    print("\nAvailable Events:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event['date']} {event['time']} - {event['details']} @ {event['location']}")
    return True

def add_common_event(events, common_events):
    for idx, event in enumerate(common_events, start=1):
        print(f"{idx}. {event['details']} @ {event['location']}")
    print("0. Done")
    choice = int(input("\nWhich Event do you want to add? ").strip()) - 1
    if choice == -1:
        return False
    if 0 <= choice < len(events):
        event = copy.deepcopy(common_events[choice])
        event["date"] = input(f"Enter new date: ").strip()
        event["time"] = input(f"Enter new time: ").strip()
        if event["date"] != "" and event["time"] != "" and event["details"] and event["location"]:
            events.append(event)
            print("Event added successfully!")
            return True
        else:
            print("Invalid input. Event not added.")
    return False

def add_event(events):
    """Add a new event interactively."""
    print("\nAdding New Event:")
    date = input("Enter date (YYYY-MM-DD): ").strip()
    time = input("Enter time (HH:MM): ").strip()
    details = input("Enter event details: ").strip()
    location = input("Enter event location: ").strip()

    if date and time and details and location:
        events.append({"date": date, "time": time, "details": details, "location": location})
        print("Event added successfully!")
    else:
        print("Invalid input. Event not added.")

def edit_event(event):
    """Edit an event by selecting which fields to modify."""
    while True:
        print(f"{event['date']} {event['time']} - {event['details']} @ {event['location']}")
        print("\nEditing Event:")
        print(f"1. Date: {event['date']}")
        print(f"2. Time: {event['time']}")
        print(f"3. Details: {event['details']}")
        print(f"4. Location: {event['location']}")
        print("0. Done editing")

        choice = input("\nWhich field do you want to edit? (Enter number, 0 to finish): ").strip()

        if choice == "1":
            event["date"] = input(f"Enter new date [{event['date']}]: ").strip() or event["date"]
        elif choice == "2":
            event["time"] = input(f"Enter new time [{event['time']}]: ").strip() or event["time"]
        elif choice == "3":
            event["details"] = input(f"Enter new details [{event['details']}]: ").strip() or event["details"]
        elif choice == "4":
            event["location"] = input(f"Enter new location [{event['location']}]: ").strip() or event["location"]
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid number.")

    print("Event updated successfully!")

def delete_event(events, index):
    """Delete an event."""
    deleted_event = events.pop(index)
    print(f"\nDeleted event: {deleted_event['details']} on {deleted_event['date']}")

def main():
    """Interactive event manager."""
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen for better readability

    if len(sys.argv) == 2:
        file_path = sys.argv[-1]
    else:
        # Ask for a file to open
        file_path = input("Enter the event file to open (default: events.json): ").strip()
    if not file_path:
        file_path = "dist/events.json"

    events = load_events(file_path)
    changes_made = False  # Track if any changes were made
    list_events(events)

    while True:
        print("\nEvent Manager")
        print(f"Currently editing: {file_path}")
        print("1. List Events")
        print("2. Add common event")
        print("3. Add Event")
        print("4. Edit/Delete event")
        print("5. Save changes")
        print("6. Save to a different file")
        print("0. Exit")

        choice = input("\nSelect an option: ").strip()
        os.system("cls" if os.name == "nt" else "clear")

        if choice == "1":
            list_events(events)
        elif choice == "2":
            changes_made = add_common_event(events, common_events)
        elif choice == "3":
            add_event(events)
            changes_made = True
        elif choice == "4":
            if not list_events(events):
                continue
            try:
                event_num = int(input("\nEnter event number (or 0 to go back): ")) - 1
                if event_num == -1:
                    continue
                if 0 <= event_num < len(events):
                    action = input("\nDo you want to (E)dit or (D)elete this event? ").strip().lower()
                    if action == "e":
                        edit_event(events[event_num])
                        changes_made = True
                    elif action == "d":
                        delete_event(events, event_num)
                        changes_made = True
                    else:
                        print("Invalid action.")
                else:
                    print("Invalid event number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            save_events(events, file_path)
            changes_made = False
        elif choice == "6":
            new_file_path = input("\nEnter new file name to save to: ").strip()
            if new_file_path:
                if new_file_path != file_path:
                    confirm = input(f"Save to {new_file_path} instead of {file_path}? (Y/N): ").strip().lower()
                    if confirm == "y":
                        save_events(events, new_file_path)
                        file_path = new_file_path
                        changes_made = False
                else:
                    save_events(events, file_path)
                    changes_made = False
        elif choice == "0":
            if changes_made:
                save_now = input("\nYou have unsaved changes. Save before exiting? (Y/N): ").strip().lower()
                if save_now == "y":
                    save_events(events, file_path)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
