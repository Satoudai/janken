puts "じゃんけんゲーム！"
puts ""
puts "最初はグー!じゃんけん・・・・"

def game
  puts "[0]グー\n[1]チョキ\n[2]パー"
 #入力を受け取る
  player_hand = gets
 #相手は0～2のランダムな数字 
  program_hand = rand(3)
 #受け取った文字の判定
　#0～2の場合は、int型に変換
  if player_hand =~ /^[0-2]+$/
    player_hand = player_hand.to_i
  else
　#それ以外はメッセージを出して終了
    puts "0から2の数で入力して下さい"
    exit
  end

  
  jankens = ["グー", "チョキ","パー"]
  puts "あなたの手:#{jankens[player_hand]}, 相手の手:#{jankens[program_hand]}"

  #じゃんけんの勝敗判定
  if player_hand == program_hand
    puts "あいこで"
    return true
  elsif(player_hand == 0 && program_hand == 1)||(player_hand == 1 && program_hand == 2)||(player_hand == 2 && program_hand == 0)
    puts "あなたの勝ちです"
    return false

  else
    puts "あなたの負けです"
    return false
  end
end


#あいこの場合は勝つか負けるまでループする
next_game = true

while next_game
  next_game = game
end
