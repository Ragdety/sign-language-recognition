from SLAudio import SLAudio

# The text that you want to convert to audio 
mytext = 'How do you pronounce Nghia?'
mytext = 'Hi there! Welcome to the world of Pokémon! My name is Oak! People call me the Pokémon Professor! This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Others use them for fights. Myself...I study Pokémon as a profession. Your very own Pokémon adventure is about to unfold! A world of dreams and adventures with Pokémon awaits! Let\'s go!'
mytext = "Hi all, I'm Nghia. I'm a software engineer. I love coding, reading, and writing. I'm also a big fan of anime and manga. I'm currently learning Japanese and I'm planning to visit Japan next year."
mytext = "yooo what's up? im nichshay. i did some cool stuff with my friends today. we went to the beach and played volleyball. it was so much fun. i also had a great time with my family. we went to the zoo and saw a lot of animals. i love animals. i also love to play video games. i'm currently playing the legend of zelda: breath of the wild. it's a really fun game. i'm also learning how to play the guitar. i'm not very good at it yet, but i'm getting better. i'm also learning how to cook. i made some pasta the other day and it was delicious. i'm really enjoying learning new things. i'm looking forward to the future. i'm excited to see what the future holds. i hope it's full of fun and adventure. i hope i can make a lot of new friends and have a lot of new experiences. i'm really looking forward to it. i hope you are too. i hope you have a great day. see you later!"

# Language in which you want to convert 
language = 'en'

sl_audio = SLAudio(text=mytext) 
sl_audio.save("test.mp3") 
  
sl_audio.play()