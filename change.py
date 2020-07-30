# ディレクトリの拡張子を変えるプログラム
import pathlib
import shutil
import glob

def change_suffix(file_name, from_suffix, to_suffix):
    # ファイルの拡張子を得る
    sf = pathlib.PurePath(file_name).suffix
    
    # 変更対象かどうか判定する
    if sf == from_suffix:
        # ファイル名(拡張子除く)を得る
        st = pathlib.PurePath(file_name).stem

        # 変更後のファイル名を得る
        to_name = st + to_suffix

        # ファイル名を変更する
        shutil.move(file_name, to_name)

if __name__ == '__main__':
    files = glob.glob("/Users/masa/labo/統合済み古典舞踊データ/**/*.trc")
    for x in range(len(files)):
        change_suffix(files[x], '.trc', '.csv')
    print(files)