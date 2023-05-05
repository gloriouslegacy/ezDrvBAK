<h1 align="center">Windows Driver Backup/Restore
<br>

```python
#백업 실행
def do_backup(folder_selected):
    message.set('> 백업 중...')
    cmd = f'pnputil.exe /export-driver * "{folder_selected}"'
    subprocess.run(cmd, shell=True)
    message.set('> 백업 완료')
    
#복원 실행
def do_restore(folder_selected):
    message.set('> 복원 중...')
    inf_files = subprocess.check_output(f'dir /s /b "{folder_selected}\\*.inf"', shell=True).decode('cp949').split('\r\n')
    inf_files = [f for f in inf_files if f]
    for inf_file in inf_files:
        cmd = f'pnputil.exe -i -a "{inf_file}"'
        subprocess.run(cmd, shell=True)
    message.set('> 복원 완료')
```
<br>

<img align="center" src="https://user-images.githubusercontent.com/132028878/236368456-62f66541-3355-4c22-888b-2493fbb1f8df.jpg" width="800"/>
