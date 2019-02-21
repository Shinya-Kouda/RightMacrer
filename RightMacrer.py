# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import datetime

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

# 処理ファイル名の出力
#tkinter.messagebox.showinfo('○×プログラム',file)

# ファイル名に基づいたフォルダ作成
today = datetime.date.today()
today + '_' + file
# ファイル提出

# ログファイルに追記