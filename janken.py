import random
import sys
print("じゃんけんゲーム！")
print("何を出しますか？")
print("[グー　チョキ　パー]")

#日本語入力をしてもらう
a = input("あなたの選択:")

#入力内容の判定
if a == "グー":
    b = int(1)
elif a == "チョキ":
    b = int(2)
elif a == "パー":
    b = int(3)
else:
    print("グー/チョキ/パーを入力してください")
    sys.exit()

#相手はランダムにする
c = random.randint(1,3)

#勝敗判定
if b==1:
    if c==1:
        print("コンピュータ：グー　　結果：あいこ")
    elif c==2:
        print("コンピュータ：チョキ　　結果：勝ち")
    else:
        print("コンピュータ：パー　　結果：負け")
elif b==2:
    if c==1:
        print("コンピュータ：グー　　結果：負け")
    elif c==2:
        print("コンピュータ：チョキ　　結果：あいこ")
    else:
        print("コンピュータ：パー　　結果：勝ち")
elif b==3:
    if c==1:
        print("コンピュータ：グー　　結果：勝ち")
    elif c==2:
        print("コンピュータ：チョキ　　結果：負け")
    else:
        print("コンピュータ：パー　　結果：あいこ")
else:
    print("1から3の整数を入力してください")

