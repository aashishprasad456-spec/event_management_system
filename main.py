import tkinter as tk
from tkinter import ttk, messagebox
import os
import random

class FileKeeper:
    def __init__(self):
        if not os.path.exists("events.txt"):
            open("events.txt", "w").close()
        if not os.path.exists("vols.txt"):
            open("vols.txt", "w").close()
        if not os.path.exists("parts.txt"):
            open("parts.txt", "w").close()
    
    def save_ev(self, idd, nm, tp, dt, st, en, wh, mx):
        f = open("events.txt", "a")
        f.write(f"{idd}|{nm}|{tp}|{dt}|{st}|{en}|{wh}|{mx}\n")
        f.close()
    
    def save_vol(self, vid, eid, nm, em, tm):
        f = open("vols.txt", "a")
        f.write(f"{vid}|{eid}|{nm}|{em}|{tm}\n")
        f.close()
    
    def save_part(self, pid, eid, nm, em, ph, tm):
        f = open("parts.txt", "a")
        f.write(f"{pid}|{eid}|{nm}|{em}|{ph}|{tm}\n")
        f.close()
    
    def get_evs(self):
        evs = []
        try:
            f = open("events.txt", "r")
            for x in f:
                x = x.strip()
                if x:
                    p = x.split("|")
                    if len(p) == 8:
                        evs.append({"i": p[0], "n": p[1], "t": p[2], "d": p[3], "s": p[4], "e": p[5], "w": p[6], "m": p[7]})
            f.close()
        except:
            pass
        return evs
    
    def get_vols(self):
        vols = []
        try:
            f = open("vols.txt", "r")
            for x in f:
                x = x.strip()
                if x:
                    p = x.split("|")
                    if len(p) == 5:
                        vols.append({"v": p[0], "e": p[1], "n": p[2], "m": p[3], "t": p[4]})
            f.close()
        except:
            pass
        return vols
    
    def get_parts(self):
        parts = []
        try:
            f = open("parts.txt", "r")
            for x in f:
                x = x.strip()
                if x:
                    p = x.split("|")
                    if len(p) == 6:
                        parts.append({"p": p[0], "e": p[1], "n": p[2], "m": p[3], "h": p[4], "t": p[5]})
            f.close()
        except:
            pass
        return parts

class IDMaker:
    def make(self):
        c = "abc123"
        r = ""
        for i in range(6):
            r += random.choice(c)
        return r

class DoEvents:
    def __init__(self):
        self.f = FileKeeper()
        self.idm = IDMaker()
    
    def add(self, n, t, d, s, e, l, m):
        if not n:
            return False
        i = self.idm.make()
        self.f.save_ev(i, n, t, d, s, e, l, str(m))
        return True
    
    def get_all(self):
        return self.f.get_evs()
    
    def find(self, i):
        for x in self.f.get_evs():
            if x["i"] == i:
                return x
        return None

class DoVols:
    def __init__(self):
        self.f = FileKeeper()
        self.idm = IDMaker()
        self.ev = DoEvents()
    
    def add(self, e, n, m):
        if not self.ev.find(e):
            return False
        for v in self.f.get_vols():
            if v["e"] == e and v["m"] == m:
                return False
        vid = self.idm.make()
        from datetime import datetime
        tm = datetime.now().isoformat()
        self.f.save_vol(vid, e, n, m, tm)
        return True
    
    def get_all(self):
        return self.f.get_vols()

class DoParts:
    def __init__(self):
        self.f = FileKeeper()
        self.idm = IDMaker()
        self.ev = DoEvents()
    
    def add(self, e, n, m, ph):
        if not self.ev.find(e):
            return False
        # check capacity
        ev = self.ev.find(e)
        if ev:
            current = len([p for p in self.f.get_parts() if p["e"] == e])
            max_p = int(ev["m"]) if ev["m"].isdigit() else 0
            if max_p > 0 and current >= max_p:
                return False
        # check duplicate
        for p in self.f.get_parts():
            if p["e"] == e and p["m"] == m:
                return False
        pid = self.idm.make()
        from datetime import datetime
        tm = datetime.now().isoformat()
        self.f.save_part(pid, e, n, m, ph, tm)
        return True
    
    def get_all(self):
        return self.f.get_parts()

class ShowEvents:
    def __init__(self, tab, ev_mgr):
        self.mgr = ev_mgr
        self.make_gui(tab)
    
    def make_gui(self, tab):
        # main frame
        main = ttk.Frame(tab)
        main.pack(fill="both", expand=True, padx=15, pady=15)
        
        # top section
        top = ttk.LabelFrame(main, text="Add New Event")
        top.pack(fill="x", pady=(0, 15))
        
        # input fields
        self.es = {}
        labs = ["Event Name", "Category", "Date", "Start Time", "End Time", "Location", "Max People"]
        keys = ["n", "t", "d", "s", "e", "p", "m"]
        
        for i in range(len(labs)):
            row = ttk.Frame(top)
            row.pack(fill="x", pady=4, padx=10)
            ttk.Label(row, text=labs[i] + ":", width=15).pack(side="left")
            e = ttk.Entry(row)
            e.pack(side="left", fill="x", expand=True, padx=5)
            self.es[keys[i]] = e
        
        # button
        btn_row = ttk.Frame(top)
        btn_row.pack(fill="x", pady=10, padx=10)
        ttk.Button(btn_row, text="Create Event", command=self.add_ev, width=20).pack()
        
        # bottom section
        bottom = ttk.LabelFrame(main, text="All Events")
        bottom.pack(fill="both", expand=True)
        
        # treeview
        tree_frame = ttk.Frame(bottom)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tree = ttk.Treeview(tree_frame, columns=("a","b","c","d","e"), show="headings", height=12)
        self.tree.heading("a", text="ID")
        self.tree.heading("b", text="Name")
        self.tree.heading("c", text="Date")
        self.tree.heading("d", text="Location")
        self.tree.heading("e", text="Max")
        
        # scrollbar
        sc = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sc.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sc.pack(side="right", fill="y")
        
        # status
        self.status = ttk.Label(bottom, text="Ready", relief="sunken", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 10))
        
        self.load()
    
    def add_ev(self):
        n = self.es["n"].get()
        t = self.es["t"].get()
        d = self.es["d"].get()
        s = self.es["s"].get()
        e = self.es["e"].get()
        p = self.es["p"].get()
        m = self.es["m"].get()
        
        if not n:
            messagebox.showerror("Error", "Need event name")
            return
        
        if not m:
            m = "0"
        try:
            m = int(m)
        except:
            m = 0
        
        if self.mgr.add(n, t, d, s, e, p, m):
            messagebox.showinfo("Success", "Event added!")
            for x in self.es.values():
                x.delete(0, tk.END)
            self.load()
            self.status.config(text="Event added successfully")
        else:
            messagebox.showerror("Error", "Failed")
            self.status.config(text="Failed to add event")
    
    def load(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        for ev in self.mgr.get_all():
            self.tree.insert("", "end", values=(ev["i"], ev["n"], ev["d"], ev["w"], ev["m"]))
        self.status.config(text=f"Found {len(self.mgr.get_all())} events")

class ShowVols:
    def __init__(self, tab, vol_mgr):
        self.mgr = vol_mgr
        self.make_gui(tab)
    
    def make_gui(self, tab):
        main = ttk.Frame(tab)
        main.pack(fill="both", expand=True, padx=15, pady=15)
        
        top = ttk.LabelFrame(main, text="Register Volunteer")
        top.pack(fill="x", pady=(0, 15))
        
        form = ttk.Frame(top)
        form.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(form, text="Event ID:", width=12).grid(row=0, column=0, sticky="w", pady=5)
        self.eid = ttk.Entry(form, width=30)
        self.eid.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(form, text="Name:", width=12).grid(row=1, column=0, sticky="w", pady=5)
        self.nm = ttk.Entry(form, width=30)
        self.nm.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(form, text="Email:", width=12).grid(row=2, column=0, sticky="w", pady=5)
        self.em = ttk.Entry(form, width=30)
        self.em.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        form.columnconfigure(1, weight=1)
        
        btn_row = ttk.Frame(top)
        btn_row.pack(fill="x", pady=(0, 10), padx=10)
        ttk.Button(btn_row, text="Register", command=self.add_vol, width=20).pack()
        
        bottom = ttk.LabelFrame(main, text="Volunteers")
        bottom.pack(fill="both", expand=True)
        
        tree_frame = ttk.Frame(bottom)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tree = ttk.Treeview(tree_frame, columns=("a","b","c","d"), show="headings", height=12)
        self.tree.heading("a", text="Event ID")
        self.tree.heading("b", text="Name")
        self.tree.heading("c", text="Email")
        self.tree.heading("d", text="Time")
        
        sc = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sc.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sc.pack(side="right", fill="y")
        
        self.status = ttk.Label(bottom, text="Ready", relief="sunken", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 10))
        
        self.load()
    
    def add_vol(self):
        e = self.eid.get()
        n = self.nm.get()
        m = self.em.get()
        
        if not e or not n or not m:
            messagebox.showerror("Error", "Fill all fields")
            return
        
        if self.mgr.add(e, n, m):
            messagebox.showinfo("Success", "Volunteer added!")
            self.eid.delete(0, tk.END)
            self.nm.delete(0, tk.END)
            self.em.delete(0, tk.END)
            self.load()
            self.status.config(text="Volunteer registered")
        else:
            messagebox.showerror("Error", "Failed to register")
            self.status.config(text="Registration failed")
    
    def load(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        for v in self.mgr.get_all():
            t = v["t"]
            if "T" in t:
                t = t.replace("T", " ")[:16]
            self.tree.insert("", "end", values=(v["e"], v["n"], v["m"], t))
        self.status.config(text=f"Found {len(self.mgr.get_all())} volunteers")

class ShowParts:
    def __init__(self, tab, part_mgr):
        self.mgr = part_mgr
        self.make_gui(tab)
    
    def make_gui(self, tab):
        main = ttk.Frame(tab)
        main.pack(fill="both", expand=True, padx=15, pady=15)
        
        top = ttk.LabelFrame(main, text="Register Participant")
        top.pack(fill="x", pady=(0, 15))
        
        form = ttk.Frame(top)
        form.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(form, text="Event ID:", width=12).grid(row=0, column=0, sticky="w", pady=5)
        self.eid = ttk.Entry(form, width=30)
        self.eid.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(form, text="Name:", width=12).grid(row=1, column=0, sticky="w", pady=5)
        self.nm = ttk.Entry(form, width=30)
        self.nm.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(form, text="Email:", width=12).grid(row=2, column=0, sticky="w", pady=5)
        self.em = ttk.Entry(form, width=30)
        self.em.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(form, text="Phone:", width=12).grid(row=3, column=0, sticky="w", pady=5)
        self.ph = ttk.Entry(form, width=30)
        self.ph.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        
        form.columnconfigure(1, weight=1)
        
        btn_row = ttk.Frame(top)
        btn_row.pack(fill="x", pady=(0, 10), padx=10)
        ttk.Button(btn_row, text="Register Participant", command=self.add_part, width=20).pack()
        
        bottom = ttk.LabelFrame(main, text="Participants")
        bottom.pack(fill="both", expand=True)
        
        tree_frame = ttk.Frame(bottom)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tree = ttk.Treeview(tree_frame, columns=("a","b","c","d","e"), show="headings", height=12)
        self.tree.heading("a", text="Event ID")
        self.tree.heading("b", text="Name")
        self.tree.heading("c", text="Email")
        self.tree.heading("d", text="Phone")
        self.tree.heading("e", text="Time")
        
        sc = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sc.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sc.pack(side="right", fill="y")
        
        self.status = ttk.Label(bottom, text="Ready", relief="sunken", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 10))
        
        self.load()
    
    def add_part(self):
        e = self.eid.get()
        n = self.nm.get()
        m = self.em.get()
        ph = self.ph.get()
        
        if not e or not n or not m or not ph:
            messagebox.showerror("Error", "Fill all fields")
            return
        
        if self.mgr.add(e, n, m, ph):
            messagebox.showinfo("Success", "Participant added!")
            self.eid.delete(0, tk.END)
            self.nm.delete(0, tk.END)
            self.em.delete(0, tk.END)
            self.ph.delete(0, tk.END)
            self.load()
            self.status.config(text="Participant registered")
        else:
            messagebox.showerror("Error", "Failed - check event ID, capacity, or duplicate email")
            self.status.config(text="Registration failed")
    
    def load(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        for p in self.mgr.get_all():
            t = p["t"]
            if "T" in t:
                t = t.replace("T", " ")[:16]
            self.tree.insert("", "end", values=(p["e"], p["n"], p["m"], p["h"], t))
        self.status.config(text=f"Found {len(self.mgr.get_all())} participants")

class MainApp:
    def __init__(self):
        self.w = tk.Tk()
        self.w.title("Campus Event Manager")
        self.w.geometry("1000x700")
        
        self.ev_mgr = DoEvents()
        self.vol_mgr = DoVols()
        self.part_mgr = DoParts()
        
        self.setup_ui()
    
    def setup_ui(self):
        # style
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 9))
        style.configure("TLabelframe", font=("Arial", 10, "bold"))
        
        # tabs
        tabs = ttk.Notebook(self.w)
        tabs.pack(fill="both", expand=True, padx=10, pady=10)
        
        t1 = ttk.Frame(tabs)
        tabs.add(t1, text="Events")
        ShowEvents(t1, self.ev_mgr)
        
        t2 = ttk.Frame(tabs)
        tabs.add(t2, text="Volunteers")
        ShowVols(t2, self.vol_mgr)
        
        t3 = ttk.Frame(tabs)
        tabs.add(t3, text="Participants")
        ShowParts(t3, self.part_mgr)
    
    def run(self):
        self.w.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()