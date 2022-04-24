define a = Character("Announcer", color="#FAE8B6")
define b = Character("BUZZER", color="#FF0000")
define cj = Character("Cave Johnson", color="#15D4A4")
define c1 = Character("Space Core", color="#F9FF0F")
define c2 = Character("Rich (Ego Core)", color="#1EA621")
define c3 = Character("Fact Core", color="#BC0E61")
define g = Character("GLaDOS", color="#A5C2AE")
define w = Character("Wheatley", color="#16A8D1")
define t = Character("Turret", color="#FF0000")
define dt = Character("Defective Turret",color="#F8D668")

image WHT:
   "images/white.png"

image BLK:
   "images/black.png"

image p1:
   "images/pause1.png"

image p2:
   "images/pause2.png"

image p3:
   "images/pause3.png"

label start:
scene BLK
a "Good morning. You have been in suspension for -FIFTY- days. In compliance with state and federal regulations, all testing candidates in the Aperture Science Extended Relaxation Center must be revived periodically for a mandatory physical and mental wellness exercise."
a "You will hear a buzzer. When you hear the buzzer, look up at the ceiling."
scene p1
pause 1
scene p2
pause 1
scene p3
pause 1
scene BLK
b "BUZZ"
menu:
   "Look at the ceiling.":
      jump ceiling

label ceiling:
a "Good. You will hear a buzzer. When you hear the buzzer, look down at the floor."
scene p1
pause 1
scene p2
pause 1
scene p3
pause 1
scene BLK
b "BUZZ"
menu:
   "Look at the floor.":
      jump floor

label floor:
a "Good. This completes the gymnastic portion of your mandatory physical and mental wellness exercise."
a "There is a framed painting on the wall. Please go stand in front of it."
menu:
   "Go to the painting.":
      jump painting

label painting:
a "This is art. You will hear a buzzer. When you hear the buzzer, stare at the art."
scene p1
pause 1
scene p2
pause 1
scene p3
pause 1
scene BLK
b "BUZZ"
menu:
   "Look at the art.":
      a "You should now feel mentally reinvigorated. If you suspect staring at art has not provided the required intellectual sustenance, reflect briefly on this classical music."
      scene p1
      pause 1
      scene p2
      pause 1
      scene p3
      pause 1
      scene BLK
      b "BUZZ"
      a "Good. Now please return to your bed."
      jump broken

label broken:
scene WHT
with Dissolve(1)
scene BLK
with Dissolve(1)
a "Good morning. You have been in suspension for nine nine nine nine nine..."
w "Hello? Anyone in there?"
jump wheat_loop

default to_self = "to self"
default whli = 0
default whil = ["Helloooo?", "Are you going to open the door? At any time?", "Hello? Can y--no?", "Are you going to open this door? Because it's fairly urgent.", "Oh, just open the door! [to self] That's too aggressive. Hello, friend! Why not open the door?", "[to self] Hm. Could be Spanish, could be Spanish. Hola, amigo! Abre la pureta! Donde esta--no. Um...", "Fine! No, absolutely fine. It's not like I don't have, you know, ten thousand other test subjects begging me to help them escape. You know, it's not like this place is about to EXPLODE.", "Alright, look, okay, I'll be honest. You're the LAST test subject left. And if you DON'T help me, we're both going to die. Alright? I didn't want to say it, you dragged it out of me. Alright? Dead. Dos Muerte."]
label wheat_loop:
menu:
   "Answer the door":
      jump broken_door
   "...":
      if whli > len(whil)-1:
         $ whli = 0
         $ wsyy = whil[whli]
         w "[wsyy]"
         $ whli = whli + 1
         jump wheat_loop2
      else:
         $ wsyy = whil[whli]
         w "[wsyy]"
         $ whli = whli + 1
         jump wheat_loop2

label wheat_loop2:
menu:
   "Answer the door":
      jump broken_door
   "...":
      if whli > len(whil)-1:
         $ whli = 0
         $ wsyy = whil[whli]
         w "[wsyy]"
         $ whli = whli + 1
         jump wheat_loop
      else:
         $ wsyy = whil[whli]
         w "[wsyy]"
         $ whli = whli + 1
         jump wheat_loop

label broken_door:
w "HA! I knew someone was alive in here."
w "AH! Oh. My. God. You look terribl-- ummm... good. Looking good, actually."
w "Are you okay? Are you - Don't answer that. I'm absolutely sure you're fine. There's plenty of time for you to recover. Just take it slow."
a "Please prepare for emergency evacuation."
w "Stay calm! 'Prepare' - that's all they're saying. 'Prepare.' It's all fine."
w "Alright? Don't move. I'm gonna get us out of here."
w "Oh. You MIGHT want to hang onto to something. Word of advice, up to you."
w "You alright down there? Can you hear me? Hello?"
w "Most test subjects do experience some cognitive deterioration after a few months in suspension."
w "Now you've been under for... quite a lot longer, and it's not out of the question that you might have a very minor case of serious brain damage."
w "But don't be alarmed, alright? Although, if you do feel alarm, try to hold onto that feeling because that is the proper reaction to being told you have brain damage."
w "Do you understand what I'm saying? At all? Does any of this make any sense?"
w "Just tell me, 'Yes'."
menu:
   "Jump":
      w "Okay. What you're doing there is jumping. You just... you just jumped. But nevermind. Say 'Apple'. 'Aaaapple.'"
      jump wheat_yes

default whi = 0
default whl = ["Simple word. 'Apple'.", "Just say 'Apple'. Classic. Very simple.", "Ay. Double Pee-Ell-Ee", "Just say 'Apple'. Easy word, isn't it? 'Apple'.", "How would you use it in a sentence? 'Mmm, this apple's crunchy', you might say. And i'm not even asking you for the whole sentence. Just the word 'Apple'"]
label wheat_yes:
menu:
   "Jump":
      w "Okay, you know what? That's close enough. Just hold tight."
      jump ride
   "...":
      if whi > len(whl)-1:
         w "Okay, you know what? That's close enough. Just hold tight."
         jump ride
      else:
         $ wsy = whl[whi]
         w "[wsy]"
         $ whi = whi + 1
         jump wheat_apple

label wheat_apple:
menu:
   "Jump":
      w "Okay, you know what? That's close enough. Just hold tight."
      jump ride
   "...":
      if whi > len(whl)-1:
         w "Okay, you know what? That's close enough. Just hold tight."
         jump ride
      else:
         $ wsy = whl[whi]
         w "[wsy]"
         $ whi = whi + 1
         jump wheat_yes

label ride:
w "placeholder"