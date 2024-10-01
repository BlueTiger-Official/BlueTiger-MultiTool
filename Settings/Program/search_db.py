import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import pandas as pd
import json
import os
from multiprocessing import Pool, cpu_count
import subprocess
import sys
from PIL import Image, ImageTk 
import fade

def process_file(file_path_ext_query, query):
    file_path, ext = file_path_ext_query
    results = []
    try:
        if ext == '.sql':
            results = search_sql(file_path, query)
        elif ext == '.txt':
            results = search_txt(file_path, query)
        elif ext == '.csv':
            results = search_csv(file_path, query)
        elif ext == '.json':
            results = search_json(file_path, query)
    except Exception as e:
        print(fade.water(f"Erreur lors de la recherche dans {file_path}: {e}"))
    return results

def search_sql(file_path, query):
    results = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        results = [f"{file_path}: {line.strip()}" for line in lines if query in line]
    return results

def search_txt(file_path, query):
    results = []
    encodings = ['utf-8', 'latin-1', 'ascii']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
                lines = file.readlines()
                results = [f"{file_path}: {line.strip()}" for line in lines if query in line]
            break
        except UnicodeDecodeError:
            continue
    return results

def search_csv(file_path, query):
    results = []
    df = pd.read_csv(file_path)
    results = df[df.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)].to_string(index=False).split('\n')
    results = [f"{file_path}: {result}" for result in results]
    return results

def search_json(file_path, query):
    results = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = json.load(file)
        results = search_json_recursive(data, query)
    results = [f"{file_path}: {result}" for result in results]
    return results

def search_json_recursive(data, query):
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                results.extend(search_json_recursive(value, query))
            elif query.lower() in str(value).lower():
                results.append(f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            results.extend(search_json_recursive(item, query))
    return results

class FileSearcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Searcher DB by Nkrz")
        self.root.geometry("800x600")
        self.folder_path = None
        self.use_multiprocessing = False
        self.cpu_percentage = 100
        self.results = []
        self.set_icon()
        self.create_widgets()
        self.config()

    def set_icon(self):
        icon_path = os.path.join('..', 'config', 'nkrz.png')
        self.root.iconphoto(False, tk.PhotoImage(file=icon_path))
        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(False, icon)

    def create_widgets(self):
        self.root.config(bg='black')
        self.folder_frame = tk.Frame(self.root, bg='black')
        self.folder_frame.pack(pady=20)

        self.folder_label = tk.Label(self.folder_frame, text="Sélectionner le dossier contenant les fichiers:", bg='black', fg='white', font=('Helvetica', 14, 'bold'))
        self.folder_label.pack(pady=10)

        self.select_folder_button = tk.Button(self.folder_frame, text="Choisir Dossier", command=self.open_folder, bg='red', fg='white', font=('Helvetica', 12, 'bold'))
        self.select_folder_button.pack(pady=5)

        self.folder_path_label = tk.Label(self.folder_frame, text="Aucun dossier sélectionné", bg='black', fg='white')
        self.folder_path_label.pack(pady=5)

        self.action_frame = tk.Frame(self.root, bg='black')
        self.action_frame.pack(pady=20)
        self.action_frame.pack_forget()

        menu_bar = tk.Menu(self.root, background='black', foreground='white')
        self.root.config(menu=menu_bar)

        self.action_menu = tk.Menu(menu_bar, tearoff=0, background='black', foreground='white')
        menu_bar.add_cascade(label="Actions", menu=self.action_menu)
        self.action_menu.add_command(label="Configurer Multiprocessing", command=self.configure_multiprocessing, background='red', foreground='white')

        self.search_label = tk.Label(self.action_frame, text="Rechercher:", bg='black', fg='white', font=('Helvetica', 14, 'bold'))
        self.search_label.pack(pady=10)

        self.search_entry = tk.Entry(self.action_frame, width=80, bg='white', fg='black', font=('Helvetica', 12))
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(self.action_frame, text="Démarrer Recherche", command=self.search_files, bg='red', fg='white', font=('Helvetica', 12, 'bold'))
        self.search_button.pack(pady=5)

        self.results_text = tk.Text(self.action_frame, wrap=tk.WORD, height=20, bg='black', fg='green', font=('Helvetica', 12))
        self.results_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.save_button = tk.Button(self.action_frame, text="Enregistrer les Résultats", command=self.prompt_save_results, bg='red', fg='white', font=('Helvetica', 12, 'bold'))
        self.save_button.pack(pady=5)

    def config(self):
        self.folder_path = os.path.join(os.path.dirname(__file__), '..', '..', 'input', 'database')

        response = messagebox.askquestion("Configuration Initiale", "Voulez-vous configurer le chemin du dossier et le multiprocessing maintenant?")
        if response == 'yes':
            self.open_folder()
            self.configure_multiprocessing()
        else:
            self.folder_path_label.config(text=f"Dossier sélectionné: {self.folder_path}")
            print(fade.water(f"Dossier par défaut sélectionné: {self.folder_path}"))
            self.folder_frame.pack_forget()
            self.action_frame.pack(pady=20)

    def open_folder(self):
        self.folder_path = filedialog.askdirectory()
        if not self.folder_path:
            messagebox.showwarning("Avertissement", "Aucun dossier sélectionné.")
            return

        if not any(os.scandir(self.folder_path)):
            messagebox.showwarning("Avertissement", "Le dossier sélectionné est vide.")
            return

        self.folder_path_label.config(text=f"Dossier sélectionné: {self.folder_path}")
        self.folder_frame.pack_forget()
        self.action_frame.pack(pady=20)
        print(fade.water(f"Dossier sélectionné: {self.folder_path}"))

    def configure_multiprocessing(self):
        response = messagebox.askquestion("Multiprocessing", "Voulez-vous utiliser le multiprocessing pour accélérer la recherche?")
        if response == 'yes':
            self.use_multiprocessing = True
            percent = simpledialog.askinteger("Configuration du multiprocessing", "Quel pourcentage de la capacité de traitement souhaitez-vous attribuer (0-100)?", minvalue=0, maxvalue=100)
            if percent is None:
                return
            self.cpu_percentage = percent
        else:
            self.use_multiprocessing = False

    def search_files(self):
        if not self.folder_path:
            messagebox.showwarning("Avertissement", "Veuillez ouvrir un dossier d'abord.")
            return

        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Avertissement", "Veuillez entrer une requête de recherche.")
            return

        self.results_text.delete('1.0', tk.END)
        print(fade.water(f"Début de la recherche pour '{query}' dans le dossier {self.folder_path}"))

        files_to_search = [(os.path.join(root_dir, file), os.path.splitext(file)[1].lower()) 
                           for root_dir, _, files in os.walk(self.folder_path) 
                           for file in files]

        if self.use_multiprocessing:
            num_workers = max(1, (cpu_count() * self.cpu_percentage) // 100)
            with Pool(num_workers) as pool:
                results = []
                for file_path_ext_query in files_to_search:
                    print(fade.water(f"Recherche dans le fichier: {file_path_ext_query[0]}"))
                    results.extend(pool.starmap(process_file, [(file_path_ext_query, query)]))
                self.results = [result for sublist in results for result in sublist]
        else:
            self.results = []
            for file_path, ext in files_to_search:
                print(fade.water(f"Recherche dans le fichier: {file_path}"))
                results = process_file((file_path, ext), query)
                self.results.extend(results)

        self.display_results(self.results)
        print(fade.water("Recherche terminée."))
        self.prompt_save_results()

    def display_results(self, results):
        if results:
            self.results_text.insert(tk.END, "\n".join(results))
        else:
            self.results_text.insert(tk.END, "Aucun résultat trouvé.")

    def prompt_save_results(self):
        response = messagebox.askquestion("Enregistrer les Résultats", "Voulez-vous enregistrer les résultats?")
        if response == 'yes':
            self.save_results()

    def save_results(self):
        if not self.results:
            messagebox.showwarning("Avertissement", "Aucun résultat à sauvegarder.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not save_path:
            return

        with open(save_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(self.results))
        print(fade.water(f"Résultats sauvegardés dans: {save_path}"))


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearcherApp(root)
    root.mainloop()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')