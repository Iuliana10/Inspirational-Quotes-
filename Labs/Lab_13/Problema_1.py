#Scrie un script Python care sa automatizeze redenumirea fisierelor dintr-un folder
#specificat. Fiecare fisier ar trebui sa primeasca un prefix „renamed_” urmat de numele
#original. De exemplu, daca exista un fisier numit „document.txt”, acesta ar trebui sa fie
#redenumit in „renamed_document.txt”.
import os

def rename_files_in_folder(folder_path):
    try:
        if not os.path.isdir(folder_path):
            print(f"Folderul '{folder_path}' nu există.")
            return

        files = os.listdir(folder_path)

        for file_name in files:
            old_path = os.path.join(folder_path, file_name)
            if os.path.isfile(old_path):
                new_name = f"renamed_{file_name}"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                print(f"Redenumit: {file_name} -> {new_name}")

        print("Procesul de redenumire s-a încheiat cu succes!")
    except Exception as e:
        print(f"Eroare: {e}")


folder = "test_folder"
rename_files_in_folder(folder)
