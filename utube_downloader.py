import tkinter as tk
from tkinter import filedialog,messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error","Please enter a valid URL")
        return
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        
        # Ask user where to save the file
        save_path = filedialog.askdirectory()
        if save_path:
            stream.download(save_path)
           # messagebox.showinfo("Success","Video downloaded successfully")
            messagebox.showinfo("Success",f"downloaded : \n{yt.title}")
        else:
            messagebox.showwarning("Cancelled","Download canceled")
            
    except Exception as e:
        messagebox.showerror("Error",f"something went wrong!\n{e}")
        
root=tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")
root.configure(bg="#f0f0f0")    

tk.Label(root,text="Enter YouTube URL:",font=("Helvetica",12,"bold"),bg="#f0f0f0").pack(pady=10)
url_entry=tk.Entry(root,width=50,font=("Helvetica",12))
url_entry.pack(pady=5)

download_btn=tk.Button(root,text="Download",command=download_video,
                       font=("Helvetica",12))
download_btn.pack(pady=10)

root.mainloop()



        

            
    