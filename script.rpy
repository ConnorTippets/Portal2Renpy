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

image wheatley:
   "images/wheatley.png"

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
show wheatley at truecenter
with Dissolve(0.2)
w "Hello? Anyone in there?"
jump wheat_loop


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

transform trueright:
   yalign 0.5
   xalign 1.0

transform center_to_right:
   linear 3.0 yalign 0.5 xalign 0.5
   linear 3.0 yalign 0.5 xalign 1.0

label broken_door:
show wheatley at trueright
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
a "All reactor core safeguards are now non-functional. Please prepare for reactor core meltdown."
w "Alright, I wasn't going to mention this to you, but I am in PRETTY HOT WATER here."
w "How you doing down there? You still holding on?"
w "The reserve power ran out, so of course the whole relaxation center stops waking up the bloody test subjects."
w "Hold on! This is a bit tricky!"
w "And of course nobody tells ME anything. Noooo. Why should they tell me anything?"
w "Why should I be kept informed about the life functions of the ten thousand bloody test subjects I'm supposed to be in charge of?"
w "Oi, it's close... can you see? Am I gonna make it through? Have I got enough space?"
w "Agh, just... I just gotta get it through here..."
w "Okay, I've just gotta concentrate!"
w "And whose fault do you think it's going to be when the management comes down here and finds ten thousand flipping vegetables?"
w "Aggh, see, now I hit that one, I hit that one..."
w "Okay, listen, we should get our stories straight, alright?"
w "If anyone asks -- and no one's gonna ask, don't worry -- but if anyone asks, tell them as far as you know, the last time you checked, everyone looked pretty much alive."
w "Alright? Not dead."
w "Okay, almost there. On the other side of that wall is one of the old testing tracks."
w "There's a piece of equipment in there we're gonna need to get out of here. I think this is a docking station. Get ready..."
w "*smashes cart into wall*"
w "Good news: that is NOT a docking station. So there's one mystery solved."
w "I'm going to attempt a manual override on this wall. Could get a bit technical! Hold on!"
w "*smashes into wall again*"
w "Almost there! Remember: you're looking for a gun that makes holes."
w "Not bullet holes, but-- well, you'll figure it out. Really do hold on this time!"
w "*smashes into wall YET AGAIN*"
w "Whew. There we go! Now I'll be honest, you are probably in no fit state to run this particular type of cognitive gauntlet."
w "But... um... at least you're a good jumper. So... you've got that."
w "You've got the jumping on your side. Just do your best, and I'll meet you up ahead."
jump wheat_jumping

default whlii = 0
default whill = ["Alright, off you go!", "Go on. Just... March on through that hole.", "Yeah, it's alright. Go ahead.", "I know I've painted quite a grim picture of your chances. But if you simply stand here, we will both surely die.", "So, once again, just... move along. One small step and everything.", "Go on.", "On ya go.", "Your destination's probably not going to come meet us here. Is it? So go on."]

label wheat_jumping:
menu:
   "Jump":
      w "That's the spirit!"
      w "Good luck!"
      jump relaxation
   "...":
      if whlii > len(whill)-1:
         menu:
            "Jump":
               w "That's the spirit!"
               w "Good luck!"
               jump relaxation
      else:
         $ wsy = whill[whlii]
         w "[wsy]"
         $ whlii = whlii + 1
         jump wheat_jumping2

label wheat_jumping2:
menu:
   "Jump":
      w "That's the spirit!"
      w "Good luck!"
      jump relaxation
   "...":
      if whlii > len(whill)-1:
         menu:
            "Jump":
               w "That's the spirit!"
               w "Good luck!"
               jump relaxation
      else:
         $ wsy = whill[whlii]
         w "[wsy]"
         $ whlii = whlii + 1
         jump wheat_jumping

label relaxation:
hide wheatley
a "Hello, and again, welcome to the Aperture Science Enrichment Center."
a "We are currently experiencing technical difficulties due to circumstances of potentially apocalyptic significance beyond our control."
a "However, thanks to Emergency Testing Protocols, testing can continue."
a "These pre-recorded messages will provide instructional and motivational support."
a "So that science can still be done, even in the event of environmental, social, economic, or structural collapse."
a "The portal will open and emergency testing will begin in three. Two. One."
a "Cube- and button-based testing remains an important tool for science, even in a dire emergency."
a "If cube- and button-based testing caused this emergency, don't worry."
a "The odds of this happening twice are very slim."
a "Please note the incandescent particle field across the exit."
a "This Aperture Science Material Emancipation Grill will vaporize any unauthorized equipment that passes through it."
"You look around. You see a door in front of you, a cube to the side, and a button directly in front of you."

label testchamb0men:
menu:
   "Go to the exit":
      "The puzzle is not solved. Try again."
      jump testchamb0men
   "Pick up the cube":
      "You have picked up a cube."
      jump testchamb0men1
   "Stand on the button":
      "The door opens, but when you try to go in, it closes. Try again."
      jump testchamb0men

label testchamb0men1:
menu:
   "Go to the exit":
      "The puzzle is not solved. Try again."
      jump testchamb0men1
   "Stand on the button":
      "The door opens, but when you try to go in, it closes. Try again."
      jump testchamb0men1
   "Put the cube on the button":
      "The door opens, and stays open."
      jump testchamb0men2

label testchamb0men2:
menu:
   "Go to the exit":
      "The puzzle is solved. Go through."
      jump testchamb1

label testchamb1:
a "If you feel liquid running down your neck, relax, lie on your back, and apply immediate pressure to your temples."
a "You are simply experiencing a rare reaction in which the Material Emancipation Grill may have emancipated the ear tubes inside your head."
"You look around. You see three buttons on pedestals that you assume you have to hit."
"You also see three glass containers with a standing button, an exit, and a cube."

default testchamb1cube = False
default testchamb1empty = False
label testchamb1men:
menu:
   "Press the button":
      "A portal opens behind you."
      jump testchamb1menp1
   "Press the button":
      "A portal opens behind you."
      jump testchamb1menp2
   "Press the button":
      "A portal opens behind you."
      jump testchamb1menp3

label testchamb1menp1:
menu:
   "Go through the portal":
      "The portal leads you to a room with a button."
      if not testchamb1cube:
         jump testchamb1menpd110
      else:
         jump testchamb1menpd111
   "Press the button":
      "A portal changes behind you."
      jump testchamb1menp2
   "Press the button":
      "A portal changes behind you."
      jump testchamb1menp3

label testchamb1menpd110:
menu:
   "Stand on the button":
      "The door opens, but its impossible to get from here to the door without it closing."
      jump testchamb1menpd110
   "Go back through the portal":
      "You're back to the room with the three buttons."
      jump testchamb1menp1

label testchamb1menpd111:
menu:
   "Stand on the button":
      "The door opens, but its impossible to get from here to the door without it closing."
      jump testchamb1menpd111
   "Put the cube on the button":
      "The door opens, and stays open"
   "Go back through the portal":
      "You're back to the room with the three buttons."
      jump testchamb1menp1

label testchamb1menp2:
menu:
   "Press the button":
      "A portal changes behind you."
      jump testchamb1menp1
   "Go through the portal":
      "The portal leads you to a room with a door."
      if not testchamb1cube:
         "The puzzle is not solved. Go back."
         jump testchamb1menp2
      else:
         "The puzzle is solved. You go through."
         jump testchamb1end
   "Press the button":
      "A portal changes behind you."
      jump testchamb1menp3

label testchamb1menp3:
menu:
   "Press the button":
      "A portal changes behind you."
      jump testchamb1menp1
   "Press the button":
      "A portal changes behind you."
      jump testchamb1menp2
   "Go through the portal":
      if not testchamb1cube:
         "The portal leads you to a room with a cube."
         jump testchamb1menpd31
      else:
         "The portal leads to an empty room (Hint: go to the door room)"
         $ testchamb1empty = True
         jump testchamb1menpd32

label testchamb1menpd31:
menu:
   "Pick up the cube":
      "You have picked up a cube"
      $ testchamb1cube = True
      jump testchamb1menpd32
   "Go through the portal":
      "You're back in the room with the three buttons."
      jump testchamb1men

label testchamb1menpd32:
menu:
   "Go through the portal":
      if testchamb1empty:
         "You're back in the room with the three buttons."
         jump testchamb1menp3
      else:
         "After collecting the cube, you're back in the room with the three buttons."
         jump testchamb1menp3

label testchamb1end:
a "Good!"
a "Because of the technical difficulties we are currently experiencing, your test environment is unsupervised."
a "Before re-entering a relaxation vault at the conclusion of testing, please take a moment to write down the results of your test."
a "An Aperture Science Reintegration Associate will revive you for an interview when society has been rebuilt."
