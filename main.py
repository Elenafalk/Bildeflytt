import os
import PySimpleGUI as GUI
from pathlib import Path
from datetime import datetime

# Build the layout.
GUI.theme("DarkGrey13")
layout = [[GUI.Text("Velg hvilke mapper du vil flytte bilder fra og til."
                    "\nALLE bilder av typen .JPG i BEGGE mappene vil endre navn til dagen bildet ble tatt."
                    "\nTrykk på startknappen når du vil begynne.\n")],
          [GUI.Text("Fra mappe", size=(8, 1)), GUI.Input(key='-FROM-', enable_events=True), GUI.FolderBrowse("Velg")],
          [GUI.Text("Til mappe", size=(8, 1)), GUI.Input(key='-TO-', enable_events=True), GUI.FolderBrowse("Velg")],
          [GUI.Submit("Start")],
          [GUI.Output(size=(80, 10), key='-OUTPUT-')]]
# Make the window.
window = GUI.Window("Rediger bildenavn", layout, margins=(100, 50))


# Function to rename all images in the given folder and move them to the other given one.
def rename_images(from_folder, to_folder):
    print("Starter flytting og endring av navn...")

    # In order to sort the images, we need to add them to a list.
    all_photos = []
    no_jpgs = 1
    for each_path in Path(from_folder).iterdir():
        if each_path.suffix == ".JPG":
            all_photos.append(each_path)
            no_jpgs = 0
    if no_jpgs == 1:
        print("Fant ingen bilder av type .JPG i " + from_folder + ".")
        return
    # There may already be images in the folder we send them to. Create a temporary directory to handle them.
    # If there's already a temp directory that's empty, we can use that one.
    temp_directory = to_folder + "/temp"
    if not os.path.isdir(temp_directory):
        os.mkdir(temp_directory)
    elif len(os.listdir(temp_directory)) == 0:
        temp_directory = temp_directory + "1"
        os.mkdir(temp_directory)
    for each_existing_path in Path(to_folder).iterdir():
        if each_existing_path.suffix == ".JPG":
            temp_path = to_folder + "/temp/" + os.path.basename(each_existing_path)
            os.rename(each_existing_path, temp_path)
    # Remember all the files from the temporary directory.
    for each_temp_path in Path(temp_directory).iterdir():
        if each_temp_path.suffix == ".JPG":
            all_photos.append(each_temp_path)
    # Now we want to sort the files based on their modified dates.
    all_photos.sort(key=lambda a: datetime.fromtimestamp(a.stat().st_mtime))
    previous_date = ""
    previous_version = 0
    for each_photo in all_photos:
        if each_photo.suffix == ".JPG":
            print("Flytter " + str(each_photo))

            # Get the creation date.
            info = each_photo.stat()
            dt = datetime.fromtimestamp(info.st_mtime)
            formatted_dt_no_sub = str(datetime.strftime(dt, "%Y%m%d_%H%M%S"))
            formatted_dt_no_version = formatted_dt_no_sub
            # If the previous photo was taken the same second, deem this another version of that one.
            if previous_date == formatted_dt_no_version:
                this_version = previous_version + 1
                formatted_dt_no_sub = formatted_dt_no_sub + "(" + str(this_version) + ")"
            else:
                this_version = 0
            # Format the file.
            formatted_dt = formatted_dt_no_sub + ".JPG"
            # Remember relevant information.
            previous_date = formatted_dt_no_version
            previous_version = this_version
            # Move and rename the file.
            try:
                os.rename(each_photo, to_folder + "/" + formatted_dt)
            except WindowsError:
                print("Ett eller flere bilder hadde samme navn. Gir dem versjon (x).")
                formatted_dt = formatted_dt_no_sub + "(x).JPG"
                os.rename(each_photo, to_folder + "/" + formatted_dt)
            print("til " + to_folder + "/" + formatted_dt)
        else:
            previous_version = 0
    if len(os.listdir(temp_directory)) == 0:
        try:
            os.rmdir(temp_directory)
            print("Rydder opp midlertidig mappe.")
        except WindowsError:
            print("Kunne ikke slette midlertidig mappe.")
    else:
        print("En midlertidig mappe ble brukt, men kunne ikke slettes igjen."
              "Det kan hende bilder ligger igjen i mappen " + temp_directory)
    print("Ferdig.")


# Create an event loop.
while True:
    event, values = window.read()
    # End program if user closes window.
    if event == GUI.WIN_CLOSED:
        break
    if event == "Start":
        if not values["-FROM-"]:
            print("Du har ikke valgt en mappe som inneholder bilder du vil flytte og endre navn på.")
        elif not values["-TO-"]:
            print("Du har ikke valgt en mappe du vil flytte bildene til.")
        elif values["-FROM-"] == values["-TO-"]:
            print("Til- og fra-mappe må være forskjellig.")
        else:
            rename_images(values["-FROM-"], values["-TO-"])

window.close()
