import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
    
#백업 다이얼로그
def backup():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        backup_thread = threading.Thread(target=do_backup, args=(folder_selected,))
        backup_thread.start()

#백업 실행
def do_backup(folder_selected):
    message.set('> 백업 중...')
    cmd = f'pnputil.exe /export-driver * "{folder_selected}"'
    subprocess.run(cmd, shell=True)
    message.set('> 백업 완료')
    
#복원 다이얼로그
def restore():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        restore_thread = threading.Thread(target=do_restore, args=(folder_selected,))
        restore_thread.start()

#복원 실행
def do_restore(folder_selected):
    message.set('> 복원 중...')
    inf_files = subprocess.check_output(f'dir /s /b "{folder_selected}\\*.inf"', shell=True).decode('cp949').split('\r\n')
    inf_files = [f for f in inf_files if f]
    for inf_file in inf_files:
        cmd = f'pnputil.exe -i -a "{inf_file}"'
        subprocess.run(cmd, shell=True)
    message.set('> 복원 완료')

def on_closing():
    if messagebox.askokcancel("종료", "프로그램을 종료하시겠습니까?"):
        window.destroy()

window = tk.Tk()
window.title("WINDOWS 드라이버 백업/복원")
window.geometry('340x100')
window.resizable(False, False)
message = tk.StringVar()
message.set('> 백업/복원 폴더를 선택하세요.')

backup_button = tk.Button(window, text="백업", overrelief="sunken", activebackground="gray",activeforeground="white",command=backup)
# backup_button.grid(row=0,column=1,padx=10,pady=10)
# backup_button.pack(side=tk.LEFT,padx=10,pady=10)
backup_button.place(x=10,y=20,width=100)

restore_button = tk.Button(window, text="복원", overrelief="sunken", activebackground="gray",activeforeground="white", command=restore)
# restore_button.place(x=140,y=20)
# restore_button.pack(side=tk.LEFT, padx=10)
restore_button.place(x=120,y=20,width=100)

exit_button = tk.Button(window, text="종료", overrelief="sunken", activebackground="gray",activeforeground="white", command=window.destroy)
# exit_button.pack(side=tk.LEFT,padx=10)
# exit_button.grid(row=0,column=3,padx=10,pady=10)
exit_button.place(x=230,y=20,width=100)

message_label = tk.Label(window, textvariable=message)
# message_label.grid(row=3,column=2,padx=10,pady=10)
# message_label.pack(side=tk.BOTTOM, pady=10)
message_label.place(x=10,y=60)

# window.iconbitmap('/Users/bigboss01/Downloads/jw_20230411/77649.ico')

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
