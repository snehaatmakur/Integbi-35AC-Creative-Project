answer = None

def question_and_answer():
    choices = [1, 2, 3, 4]
    
    while True:
        answer = input("Please make a choice: ")
        try:
            answer = int(answer)
            if answer in choices:
                break
            else:
                print("Invalid input: Please enter a number (1, 2, 3, 4).")
        except ValueError:
            print("Invalid input: Please enter a valid number.")
    return answer

def congratulations_screen():
    print("\n🎉 Congratulations! 🎉\n")
    print("You have successfully led your people through deserts, mountains, jungles, and icy tundras.")
    print("You survived raging storms, wild animals, freezing winters, and food shortages.")
    print("Through teamwork, bravery, and clever choices, you helped humanity spread across the globe!\n")
    print("🌍 Your journey mirrors the incredible real story of human migration — a story of courage, adaptation, and discovery.")
    print("Thanks to explorers like you, future generations will build homes, create art, invent tools, and form communities across every continent!\n")
    print("👉 Fun Fact: Every human alive today can trace their ancestry back to these ancient migrations!\n")
    print("🏹 🛖 🎨 🌾 🧵 🔥 🚣‍♀️\n")
    print("The adventure of humanity has only just begun. Will you lead the next journey?")


def try_again_screen():
    print("\n❌ Game Over... But Not the End! ❌\n")
    print("Every journey has challenges — and even the greatest explorers faced setbacks.")
    print("Don't give up! 🌟\n")
    print("Your ancestors survived by adapting, learning, and trying again. Now it's your turn!\n")
    print("👉 Fun Fact: Early humans didn't succeed on their first try either — they spent thousands of years exploring, failing, and thriving through determination!\n")
    print("🔄 Go back, make new choices, and lead your people to survival!")
    print("🏹 🔥 🛖 🌾 🎨\n")


print("Welcome to the The Human Journey!\nYou will start your journey as a Homo Sapien in East Africa 200,000 years ago!")
print("\nYou and your family are early humans living in warm, sunny East Africa.\nThe rivers are full of fish. You have tools, fire, and friends. But you wonder...")

print("\n🗨️ Should we explore beyond the mountains? What is out there?")
print("\n➡️ Choose your path:")
print("\n1. Stay in Africa\n2. Go to Europe\n3. Go to Asia\n4. Go to Northern America")
print("To answer, type in the number associated with your choice! Good luck!!")
answer = question_and_answer()

if answer == 1: # Stay in Africa
    print("\nYou stay and explore your giant, beautiful homeland, Africa!")
    print("\nFact: Humans first evolved in Africa about 300,000 years ago and have lived there longer than\nanywhere else​.")
    print("Fact: Africa has the highest genetic, linguistic, and cultural diversity in the world​!")
    print("\nWould you like to travel to...?")
    print("1. North Africa\n2. West Africa\n3. South Africa")
    answer = question_and_answer()
    if answer == 1: # North Africa
        print("\nYou walk north through dry, hot deserts.\n🗨️ It’s hard to find water... but if we follow the stars, we might reach an oasis!")
        print("\n🛑 Obstacle: You run out of water-but you meet Neanderthals! You speak different languages\nand need to share water.")
        print("You can either...")
        print("1. Use signs and drawings\n2. Trade your tools\n3. Scare them off")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou draw water drops in the dirt and point to your mouth. The Neanderthals\npause… then one of them draws a stream.")
            print("Together, you follow them to a small spring. You drink, rest, and even learn some\nof their signs.")
            print("You survive and gain new allies for the journey ahead.")
            congratulations_screen()
        elif answer == 2:
            print("\nYou show them your sharp stones and spears. At first, they don’t\nunderstand—but then one of them offers you a shell full of water.")
            print("You trade and gain their trust. They even show you new ways to hunt and cook.")
            print("\nFact: Early North African people made jewelry from shells and bones — some of\nthe oldest jewelry in the world!​")
            print("Fact: Humans and Neanderthals interacted and even interbred in some regions​")
            print("\nYou finally reach an oasis and meet Neanderthals coming from Europe!")
            congratulations_screen()
        elif answer == 3:
            print("\nYou raise your voice and wave your arms. The Neanderthals grow angry.")
            print("They throw rocks and chase your group away.")
            print("Without water, you collapse from thirst.")
            try_again_screen()
    elif answer == 2: # West Africa
        print("\nYou walk through thick jungles filled with sound and life.\n🗨️ Watch out for snakes and wild animals!")
        print("\n🛑 Obstacle: Flooded rivers block your path!")
        print("You can either...")
        print("1. Build a raft from trees?\n2. Walk along the river to find a shallow spot?\n3. Try to swim across the fast water")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou gather logs and vines, working with your group to build a raft.")
            print("The raft floats safely across the river!")
            print("You invent better spears and tools, and your music echoes through the trees as\nyou continue your journey.")
            print("\nFact: Early West African cultures made early drums that could send messages\nacross long distances​!")
            congratulations_screen()
        elif answer == 2:
            print("\nYou walk for hours, following the sound of rushing water.")
            print("Eventually, you find a place where the river is narrow and calm. You cross it\ncarefully.")
            print("You learn how to track animals near water and spot signs of changing\nseasons—skills that help your group thrive.")
        elif answer == 3:
            print("\nThe current is stronger than it looks…")
            print("You’re swept away! You don’t make it across")
            try_again_screen()
    elif answer == 3: # South Africa
        print("\nYou follow elephants to a land of rivers and caves.\n🗨️ Let’s paint the animals we see to teach others.")
        print("🛑 Obstacle: A thunderstorm washes away your trail.")
        print("You can either...")
        print("1. Try to walk through the storm and keep moving forward?\n2. Climb higher to see the path?\n3. Stay in a cave until the storm passes?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou decide to brave the storm, but the rain makes the path too slippery. You lose\nyour footing and fall into a ravine.")
            print("You hurt yourself badly and are forced to rest for a long time.")
            try_again_screen()
        elif answer == 2:
            print("\nYou scramble up the rocky hills, fighting the wind and rain. Once you reach the\ntop, the storm clears for a moment, and you spot the path again.")
            print("You find new routes through the mountains and gain a better understanding of\nthe landscape.")
            print("You successfully navigate through the storm, discovering new territories to\nexplore.")
        elif answer == 3:
            print("\nYou take shelter in a nearby cave, waiting for the thunderstorm to subside.\nInside, you rest and gather your thoughts.")
            print("Once the storm ends, you venture out to explore the surrounding area,\ndiscovering footprints and animal tracks along the way.")
            print("\nFact: Some of the world’s oldest paint materials were used by early artists in\nSouth Africa over 70,000 years ago​!")
            congratulations_screen()

elif answer == 2: # Go to Europe
    print("\nYou have chosen to travel to Europe")
    print("You leave Africa through the Sinai Peninsula and cross into the Middle East. It's rocky and dry.")
    print("\nWould you like to travel to...?")
    print("1. Middle East\n2. Northern Europe\n3. Southern Europe")
    answer = question_and_answer()
    if answer == 1: # Middle East
        print("\nYou reach the middle east!")
        print("🗨️ Let’s find caves or build huts. We need shade and water.")
        print("\n🛑 Obstacle: A sandstorm is coming!")
        print("You can either...")
        print("1. Find shelter fast?\n2. Keep moving and cover your face")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou quickly spot a rock formation and take cover behind it just in time. The\nsandstorm rages on, but you’re safe and protected.")
            print("Once the storm passes, you venture out and discover wild sheep grazing nearby.")
            print("You begin building stone homes to stay safe in the future.")
            print("\nFact: Early people in the Middle East began shaping stones into sharp blades,\npaving the way for advanced hunting​.")
            print("Fact: The Middle East later became the birthplace of agriculture, with wheat and\nbarley first domesticated in the Fertile Crescent​.")
            print("\nYou learn to live with the land and its animals.")
            congratulations_screen()
        elif answer == 2:
            print("\nYou cover your face with a cloth and keep moving forward, hoping to outrun the\nstorm. But the wind is too strong, and you lose your bearings.")
            print("You wander off track and become disoriented in the storm, unable to find shelter\nin time.")
            print("You become too exhausted and have to rest.")
            try_again_screen()
    elif answer == 2: # Northern Europe
        print("\nIt’s freezing. Snow covers everything.\n🗨️ We’ll need fur, fire, and shelter fast!")
        print("\n🛑 Obstacle: Your fire won’t start in the snow!")
        print("You can either...")
        print("1. Wait for the storm to pass and hope for a warmer day?\n2. Use stones to spark a new fire?\n3. Look for dry sticks in a cave?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou decide to wait, hoping the storm will stop soon. But as the temperature drops\nfurther, the cold becomes unbearable.")
            print("Your group grows weak from hunger and cold.")
            print("You fail to protect your group from the elements.")
            try_again_screen()
        elif answer == 2:
            print("\nYou try to use stones to create a spark, but the snow keeps putting out the flame\nbefore it grows strong. After several attempts, your hands grow cold and tired.")
            print("You fail to start the fire, and now your group must search for shelter or risk\nfreezing.")
            print("You lose valuable time and warmth.")
            try_again_screen()
        elif answer == 3:
            print("\nYou search around and find a small cave nearby. Inside, you discover dry sticks\nhidden under rocks. You quickly gather them and manage to start a fire.")
            print("As the fire warms you, you begin to craft fur clothes and bone needles to survive\nthe harsh winter.")
            print("The fire not only keeps you warm but helps you create tools for survival.")
            print("\nFact: Humans in Ice Age Europe carved tiny statues and made warm shoes from\nanimal skin​.")
            print("Fact: During the Last Glacial Maximum, most of Europe was tundra, with cold\nsteppes full of mammoths and woolly rhinos​.")
            congratulations_screen()
    elif answer == 3: # Southern Europe
        print("\nYou travel to green hills where Neanderthals live.\n🗨️ Should we fight them… or be friends?")
        print("\n🛑 Obstacle: Food is running low.")
        print("You can either...")
        print("1. Trade with Neanderthals?\n2. Ignore the Neanderthals and hunt on your own?\n3. Follow a herd of deer in the forest?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou approach the Neanderthals and offer them some of your tools in exchange\nfor food. After some hesitation, they agree and trade dried meat and berries.")
            print("You sit by the fire, sharing stories and food. The exchange helps you both\nsurvive.")
            print("\nFact: In places like France, caves reveal that humans and Neanderthals lived\nand painted together​.")
            print("Fact: Early Europeans created stunning cave paintings and carved figurines like\nthe Venus of Hohle Fels​.")
            print("\nYou learn new ways to hunt and cook from them.")
            congratulations_screen()
        elif answer == 2:
            print("\nYou refuse to trade and try hunting alone. However, the forest is dense, and\ngame is scarce. You end up losing track of your group and go hungry for days.")
            print("You become too weak to continue. Your group must abandon the search for now.")
            try_again_screen()
        elif answer == 3:
            print("\nYou follow a herd of deer into the forest, hoping to catch one for food. It’s hard to\nkeep up with them, but you finally manage to trap one using a clever snare.")
            print("You have enough to feed yourself, but you’re exhausted.")
            print("You return to camp and rest before continuing your journey.")

elif answer == 3: # Go to Asia
    print("\nYou have chosen to travel to Asia")
    print("You journey through deserts, jungles, mountains, and coasts. Asia is vast and full of surprises!")
    print("\nFact: Asia has some of the oldest human fossils outside Africa, showing ancient humans lived\nacross Siberia, China, and Southeast Asia for hundreds of thousands of years​.")
    print("Fact: After leaving Africa, modern humans spread rapidly across Asia, adapting to wildly\ndifferent environments​.")
    print("Would to like to travel to...?")
    print("1. South Asia (India)\n2. East Asia (China, Korea, Japan)\n3. Siberia")
    answer = question_and_answer()
    if answer == 1: # South Asia
        print("\nYou reached India, and you settle by a mighty river.")
        print("🗨️ Let’s grow food instead of chasing it!")
        print("\n🛑 Obstacle: Monsoon rains flood your crops!")
        print("You can either...")
        print("1. Move to higher ground?\n2. Build walls to protect the plants?\n3. Do nothing and hope the rain stops")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou decide to move yourself and your crops to higher ground, hoping to avoid the\nfloodwaters. The journey is difficult, but you find a dry hill where the crops can\ngrow safely.")
            print("While it takes time to settle in, you adapt and create a new, fertile farming area.")
            print("You survive the monsoon, but it takes longer to rebuild your food stores.")
            congratulations_screen()
        elif answer == 2:
            print("\nYou gather rocks and mud to build walls around your crops. As the rains\ncontinue, the walls help keep the water from washing away the plants.")
            print("With the water held back, you build terraces on the hillside to catch the rainwater\nand protect your crops.")
            print("\nFact: Farming began along the Indus and Ganges rivers more than 10,000 years\nago!")
            print("Fact: Early South Asians likely adapted to seasonal flooding, developing some of\the first urban civilizations like those seen later at Mohenjo-Daro​.")
            print("Soon, you successfully grow wheat and rice, ensuring a steady food supply.")
            congratulations_screen()
        elif answer == 3:
            print("\nYou wait, hoping the rain will subside. Unfortunately, the floods overwhelm the\ncrops, and much of your harvest is lost.")
            print("Without food, your group struggles to survive.")
            try_again_screen()
    elif answer == 2: # East Asia
        print("\nYou reach bamboo forests with deer and rivers.")
        print("🗨️ This land is rich. Let’s stay and build.")
        print("\n🛑 Obstacle: Wild animals are eating your food at night!")
        print("You can either...")
        print("1. Stay up and scare them off?\n2. Set traps around the food?\n3. Build fences?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou stay awake at night, making loud noises and waving sticks to frighten the\nanimals away. While this keeps them at bay for a while, you’re exhausted and\nunable to rest properly.")
            print("Eventually, the animals grow smarter and begin to come back every night.")
            print("You struggle with fatigue, and your food supply begins to dwindle.")
            try_again_screen()
        elif answer == 2:
            print("\nYou set up clever traps to catch the wild animals. While this works for a few\nnights, it’s exhausting and time-consuming to maintain the traps every day.")
            print("After a while, the traps start to catch smaller animals instead of the larger ones\nyou need to protect your food.")
            print("You manage to protect your food but lose valuable time and resources.")
            try_again_screen()
        elif answer == 3:
            print("\nYou gather wood and stones to build strong fences around your food supply. The\nanimals can’t get through the barriers, and your crops are safe for the night.")
            print("With your food protected, you focus on other tasks and invent pottery, rice\nfarming, and nets for fishing.")
            print("\nFact: Ancient people in China were the first to cook noodles and brew tea!")
            print("Fact: Farming in China started independently, with early millet farming in the\nnorth and rice farming in the south​.")
            print("Fact: Japan's Jomon people, even before farming arrived, built complex societies\nwith pottery and large villages​.")
            print("You thrive as you develop new ways to store and gather food.")
            congratulations_screen()
    elif answer == 3: # Siberia
        print("\nYou cross high mountains and frozen ground of Siberia.")
        print("🗨️ The cold bites, but we must keep going.")
        print("\n🛑 Obstacle: A snowstorm blocks your path!")
        print("You can either...")
        print("1. Wait in a tent?\n2. Keep walking through the storm?\n3. Build a snow shelter")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou set up your tent and huddle together to stay warm. The storm rages on for\nhours, but you are protected from the cold.")
            print("Once the storm clears, you venture out and follow the tracks of mammoths. They\nlead you to a place where you can find food and shelter for the night.")
            print("\nFact: Humans in Siberia made warm homes with mammoth bones and furs!​")
            print("Fact: Siberia was one of the coldest places ancient humans lived, and surviving\nthere meant adapting to extreme cold and hunting giant Ice Age mammals​.")
            print("\nYou use the mammoths for food and warmth, surviving through the storm.")
            congratulations_screen()
        elif answer == 2:
            print("\nYou push forward through the snowstorm, hoping to find shelter or safety. But the\nwind is fierce, and you lose your way.")
            print("You’re exhausted and nearly frozen by the time you find cover under a rocky\noverhang.")
            print("You survive but waste precious energy and food trying to keep moving.")
            try_again_screen()
        elif answer == 3:
            print("\nYou work together to build a shelter from the snow, hoping to shield yourselves\nfrom the worst of the storm. It takes longer than expected, and the cold is\nunbearable.")
            print("After the storm subsides, you must find food and warmth fast. The delay costs\nyou time, and you struggle to gather enough supplies.")
            print("You manage to survive but are now low on resources.")
            try_again_screen()

elif answer == 4: # Go to Northern America
    print("\nYou have chosen to travel to Northern America")
    print("You cross the Bering Land Bridge from Siberia to a whole new world!")
    print("\nFact: During the Last Ice Age (the Last Glacial Maximum), sea levels were about 100 meters\nlower than today, creating a land bridge called Beringia between Asia and North America​.")
    print("Fact: Life in Beringia was harsh, but the southern coastal area was warmer and wetter than\ninland Siberia, providing food like fish and plants​.")
    print("\nAfter crossing, you find that you can travel to different area")
    print("Would to like to travel to...?")
    print("1. Alaska\n2. The Great Plains\n3. Eastern Woodlands")
    answer = question_and_answer()
    if answer == 1: # Alaska
        print("\nYou have reached Alaska!\nThe land is cold but full of animals.")
        print("🗨️ We can make spears and follow the herds!")
        print("\n🛑 Obstacle: The sea ice cracks under your feet!")
        print("You can either...")
        print("1. Go around it the long way?\n2. Crawl slowly and carefully?\n3. Try to jump to the other side?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou decide to avoid the dangerous ice and walk a longer route along the coastline.\nIt takes much longer and is physically exhausting, but you stay safe.")
            print("Once you find a safer spot, you create shelters and find food, but you’re running low on supplies.")
            print("The detour costs you time and resources.")
            print("\nFact: Migration along the Pacific coast (the 'Kelp Highway') might have allowed\nearlier people to survive and move south before the ice-free corridor opened")
            try_again_screen()
        elif answer == 2:
            print("\nYou drop to your belly and move slowly, carefully testing each step on the ice.\nYour heart races as the ice shifts beneath you, but you remain calm and patient.")
            print("Eventually, you reach solid ground safely. You build igloo shelters and sleds to help you\nmove through the icy terrain.")
            print("\nFact: The Inuit people made homes and tools entirely from ice and bone!")
            print("Fact: Ancient people surviving here were likely incredibly resourceful, using every\navailable material and adapting to the intense cold.")
            print("Your survival skills help you thrive in this frozen world.")
            congratulations_screen()
        elif answer == 3:
            print("\nIn a panic, you attempt to jump across the crack. But the ice beneath you shifts\nand cracks even more, and you fall through into the freezing water.")
            print("You’re caught and must fight to stay afloat, but the cold water saps your strength\nquickly.")
            print("You didn’t make it and face the cold waters of the sea.")
            try_again_screen()
            
    elif answer == 2: # Great Plains
        print("\nYou enter grasslands filled with buffalo.")
        print("🗨️ Let’s hunt and share stories under the stars.")
        print("\n🛑 Obstacle: A herd stampede is coming!")
        print("You can either...")
        print("1. Climb a tree?\n2. Run towards a nearby river?\n3. Hide behind rocks?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou race up a tree, but the stampede is fast and relentless. The bison are too\nclose for comfort, and some of them crash into the trees as they charge by.")
            print("After the danger passes, you carefully descend, but you’ve lost valuable time and\nenergy.")
            print("You survive, but you’re exhausted and need to rest.")
            try_again_screen()
        elif answer == 2:
            print("\nYou sprint toward a nearby river, hoping the bison won’t follow you there. The\nriver is fast-flowing, but it gives you the safety you need.")
            print("Once the stampede clears, you find a safer place and begin hunting and fishing.\nHowever, you’re low on supplies and must be cautious.")
            print("\nFact: After the Ice Age, as climates warmed, people adapted their hunting\ntechniques and expanded southward into rich grasslands like the Great Plains​.")
            print("\nYou survive the stampede, but the journey ahead is still uncertain.")
            try_again_screen()
        elif answer == 3:
            print("\nYou quickly dive behind a cluster of rocks, hoping the herd doesn’t notice you.\nThe ground shakes as the massive bison charge past, but you stay safe.")
            print("Once the herd passes, you and your group use teamwork to hunt one of the\nstragglers. You make teepees and tools from every part of the bison, ensuring\nnothing goes to waste.")
            print("\nFact: Plains tribes used every part of the buffalo—for food, clothes, tools, and homes!​")
            print("Fact: Ancient bison species were even larger during the Ice Age. The early\npeoples' success in hunting these animals helped them build thriving\ncommunities across the Plains​.")
            print("\nYour survival and resourcefulness strengthen your group.")
            congratulations_screen()
    elif answer == 3: # Eastern Woodlands
        print("\nForests are full of life, and you meet many other tribes.")
        print("🗨️ Let’s build longhouses and share seeds.")
        print("\n🛑 Obstacle: A wildfire is spreading!")
        print("You can either...")
        print("1. Dig a firebreak?\n2. Head to a river?\n3. Stay and fight the fire with water?")
        answer = question_and_answer()
        if answer == 1:
            print("\nYou quickly gather tools and start digging a firebreak—removing vegetation to\nstop the fire from spreading. It’s hard work, but it pays off as the fire cannot reach\nyou.")
            print("Once the danger passes, you escape to safety and help others in need. You\ntrade corn, beans, and crafts with your neighbors, strengthening your community.")
            print("\nFact: Many Native American tribes built large towns with farming, councils, and\nmarkets.")
            print("Fact: After the glaciers receded, fertile lands in the east allowed people to farm\nimportant crops like corn, beans, and squash, supporting bigger, more complex\nsocieties​.")
            print("Your teamwork and resourcefulness help you survive and thrive.")
            congratulations_screen()
        elif answer == 2:
            print("\nYou decide to head for the river, hoping to find safety in the water. The smoke\nand heat are intense, but you manage to reach the riverbank.")
            print("You wade through the water, keeping your head down as the fire burns nearby.\nOnce you’re safe, you help those who also found shelter by the river.")
            print("Though you survive, you’ve used up much of your energy escaping.")
            try_again_screen()
        elif answer == 3:
            print("\nYou try to fight the fire by gathering water from nearby sources, but the fire\nspreads too quickly, and it’s impossible to put it out.")
            print("The flames get too close, forcing you to retreat, and you lose precious supplies in\nthe chaos.")
            print("You narrowly escape, but the damage is done, and you are now without resources.")
            try_again_screen()