import pyperclip
import webbrowser

clipboard_content = pyperclip.paste()


base_url = "https://jisho.org/search/"  
full_url = base_url + clipboard_content


webbrowser.open(full_url)

print(f"Opened URL: {full_url}")