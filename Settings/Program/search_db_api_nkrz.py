import sys
import os
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))
sys.path.insert(0, config_path)

import config

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk  

API_SEARCH = config.API_SEARCH
API_AUTH_TOKEN = config.API_AUTH_TOKEN

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recherche de Joueurs")
        self.configure(bg="#000000")

        icon_path = os.path.join(config_path, 'Nkrz.png')
        if not os.path.isfile(icon_path):
            raise FileNotFoundError(f"Le fichier {icon_path} est introuvable.")
        self.iconphoto(False, tk.PhotoImage(file=icon_path))

        self.search_frame = tk.Frame(self, bg="#000000")
        self.search_frame.pack(pady=20)

        self.search_label = tk.Label(self.search_frame, text="Termes de recherche:", font=("Helvetica", 14), fg="#ffffff", bg="#000000")
        self.search_label.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(self.search_frame, width=50, font=("Helvetica", 14), bd=2, relief=tk.SOLID, bg="#333333", fg="#ffffff")
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.search_frame, text="Rechercher", font=("Helvetica", 14), command=self.search, bg="#ff0000", fg="#ffffff", relief=tk.RAISED)
        self.search_button.pack(side=tk.LEFT, padx=10)

        self.tree = ttk.Treeview(self, columns=("Nom", "Steam", "Xbox", "Microsoft", "Discord", "FiveM", "IP", "License2", "License", "Date"), show='headings', style="Treeview")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Steam", text="Steam")
        self.tree.heading("Xbox", text="Xbox")
        self.tree.heading("Microsoft", text="Microsoft")
        self.tree.heading("Discord", text="Discord")
        self.tree.heading("FiveM", text="FiveM")
        self.tree.heading("IP", text="IP")
        self.tree.heading("License2", text="License2")
        self.tree.heading("License", text="License")
        self.tree.heading("Date", text="Date")

        style = ttk.Style()
        style.configure("Treeview",
                        background="#333333",  
                        foreground="#000000", 
                        fieldbackground="#333333",  
                        font=("Helvetica", 12))
        style.configure("Treeview.Heading",
                        background="#2c2c2c", 
                        foreground="#000000",  
                        font=("Helvetica", 12, 'bold'))
        style.map('Treeview',
                  background=[('selected', '#555555')])

        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.sort_column = None
        self.add_sorting()

        self.update_idletasks()
        self.geometry(f"{self.winfo_width()}x{self.winfo_height()}")
        self.minsize(self.winfo_width(), self.winfo_height())

    def search(self):
        search_term = self.search_entry.get()
        if not search_term:
            messagebox.showerror("Erreur", "Veuillez entrer un terme de recherche.")
            return

        try:
            response = requests.get(f"{API_SEARCH}/search-players", params={"search_term": search_term, "token": API_AUTH_TOKEN})
            response.raise_for_status()
            data = response.json()

            if data['status'] == 'success' and data['players']:
                self.tree.delete(*self.tree.get_children())
                for player in data['players']:
                    self.tree.insert("", tk.END, values=(
                        player.get('name', 'Non trouvé'),
                        player.get('steam_id', 'Non trouvé'),
                        player.get('xbl_id', 'Non trouvé'),
                        player.get('live_id', 'Non trouvé'),
                        player.get('discord_id', 'Non trouvé'),
                        player.get('fivem_id', 'Non trouvé'),
                        player.get('ip', 'Non trouvé'),
                        player.get('license2_id', 'Non trouvé'),
                        player.get('license_id', 'Non trouvé'),
                        player.get('date_added', 'Non spécifiée')
                    ))

                self.update_idletasks()
                self.geometry(f"{self.winfo_width()}x{self.winfo_height()}")
                self.minsize(self.winfo_width(), self.winfo_height())

            else:
                messagebox.showinfo("Résultat", "Aucun joueur trouvé.")

        except requests.RequestException as e:
            messagebox.showerror("Erreur", f"Erreur de connexion à l'API : {e}")

    def sort_tree(self, col, reverse):
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
        data.sort(reverse=reverse)

        for index, (val, item) in enumerate(data):
            self.tree.move(item, '', index)

        self.tree.heading(col, command=lambda: self.sort_tree(col, not reverse))

    def add_sorting(self):
        for col in self.tree["columns"]:
            self.tree.heading(col, command=lambda _col=col: self.sort_tree(_col, False))

if __name__ == "__main__":
    app = App()
    app.mainloop()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
