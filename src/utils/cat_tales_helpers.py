HEADER_TEXT = "🐾 Welcome to the Adventures of {CAT_NAME1} and {CAT_NAME2}! 🐾"
USER_INTRO_TEXT = """
Say hello to {CAT_NAME1} and {CAT_NAME2}, two {BROTHER} cats 🐱 who love playing tricks and going on fun adventures. 
{CAT_NAME1}, the older {CAT1BROTHER}, is really good at thinking up tricks 
because of {CAT1HIS} smart mind and sharp eyes. 
{CAT_NAME2}, the younger {CAT2BROTHER}, is full of excitement and bravery, 
perfect at pulling off the tricks with a twinkle in {CAT2HIS} eyes.

**Your job is to guide these two {BROTHER}s on their next adventure!**

To get started, we invite you to input a story prompt. 
This could be as magical as _"{CAT_NAME1} and {CAT_NAME2} discover a treasure map"_ or as mysterious as 
_"The {BROTHER}s accidentally get locked in the museum at night."_ 
Your prompt will set the stage for the cats' next adventure.

Once the story starts to unfold, **you** will become the director of their tale. 
At different moments in the story, you'll be presented with two choices—just 
pick the one you prefer, and watch as the adventure continues based on your selection. 📚🔍

🚀 **Ready to guide {CAT_NAME1} and {CAT_NAME2} on their next adventure? 
Please provide a story idea to begin.** 🎩🎈
"""

CAT_NAMES = [
    (("Everett", "He/Him"), ("Forrest", "He/Him")),
    (("Oscar", "He/Him"), ("Felix", "She/Her")),
    (("Odie", "She/Her"), ("The King", "He/Him")),
    (("Whiskers", "He/Him"), ("Paws", "She/Her")),
    (("Shlingy", "She/Her"), ("Licorice", "She/Her")),
    (("Gizmo", "They/Them"), ("Widget", "She/Her")),
    (("Ziggy", "They/Them"), ("Zephyr", "He/Him")),
    (("Doodle", "She/Her"), ("Sketch", "They/Them")),
    (("Tigger", "He/Him"), ("Baloo", "She/Her")),
    (("Pippin", "She/Her"), ("Merry", "He/Him")),
    (("Albus", "She/Her"), ("Sirius", "She/Her")),
    (("Loki", "He/Him"), ("Thor", "She/Her")),
    (("Merlin", "She/Her"), ("Arthur", "He/Him")),
    (("Cheshire", "She/Her"), ("Simba", "She/Her")),
    (("Jinx", "He/Him"), ("Hex", "They/Them")),
    (("Rascal", "She/Her"), ("Rogue", "He/Him")),
    (("Biscuit", "He/Him"), ("Bagel", "She/Her")),
    (("Marley", "She/Her"), ("Ziggy", "He/Him")),
    (("Gulliver", "She/Her"), ("Atlas", "She/Her")),
    (("Nemo", "He/Him"), ("Dory", "She/Her")),
    (("Chip", "He/Him"), ("Dale", "He/Him")),
    (("Cosmo", "They/Them"), ("Astro", "She/Her")),
    (("Milo", "He/Him"), ("Otis", "She/Her")),
    (("Dexter", "She/Her"), ("Max", "He/Him")),
    (("Inky", "She/Her"), ("Smudge", "She/Her")),
    (("Leo", "He/Him"), ("Lynx", "She/Her")),
]


SPINNER_MSGS = [
    "{CAT_NAME1} and {CAT_NAME2} are planning their next move...",
    "The cats are brewing their next prank...",
    "{CAT_NAME1} is busy sharpening {CAT1HIS} strategy skills...",
    "{CAT_NAME2} is conjuring up some courage...",
    "Paws for a moment - story in progress!",
    "Just a whisker away from the next adventure...",
    "The cats are on a quick tuna break...",
    "The cats are currently causing mischief...",
    "{CAT_NAME1} is mapping out your next choice...",
    "{CAT_NAME2} is scratching out the next plot twist...",
    "The cats are busy climbing the tree of imagination...",
    "Chasing a yarn ball of ideas...",
    "Navigating the rooftop of creativity...",
    "Hold on, the cats are stuck in a box... of ideas!",
    "{CAT_NAME1} is at the scratching post of brainstorming...",
    "{CAT_NAME2} is leaping to the next big adventure...",
    "Pouncing on the next part of your story...",
    "{CAT_NAME1} and {CAT_NAME2} are sneaking through the alley of thoughts...",
    "Hang tight - a hairball of ideas is being coughed up!",
    "The cats are taking a catnap to dream up the next part...",
]
SIMPLIFIED_STORY_IDEAS = [
    "{CAT_NAME1} and {CAT_NAME2} find a secret door in their house.",
    "The cats find a bird who speaks their language.",
    "{CAT_NAME1} turns invisible after finding a shiny rock.",
    "{CAT_NAME2} gets stuck in a tree and {CAT_NAME1} must help {CAT2HIM}.",
    "The cats find a secret map in their toy box.",
    "{CAT_NAME1} and {CAT_NAME2} visit a world where cats are in charge.",
    "The cats find a hidden door in the backyard.",
    "{CAT_NAME1} and {CAT_NAME2} ride a big balloon to the sky.",
    "{CAT_NAME2} can only speak in rhymes after meeting a funny witch.",
    "{CAT_NAME1} finds a special collar that gives {CAT1HIM}} three wishes.",
    "The cats become superheroes for a day after finding a magic cape.",
    "The cats are mistaken for aliens by the neighborhood dogs.",
    "The cats find a magical lamp in the attic.",
    "The cats find a chest full of toys in their sandbox.",
    "{CAT_NAME2} turns everything he touches into fish after making a wish.",
    "{CAT_NAME1} learns to talk to humans for a day.",
    "{CAT_NAME1} and {CAT_NAME2} help a ghost find his house.",
    "The cats find a tunnel that leads to a magic forest.",
    "The cats switch bodies for a day after finding a magic stone.",
    "The cats find a flying potion in a cookbook.",
    "{CAT_NAME1} and {CAT_NAME2} find a big dragon in the basement.",
    "The cats go on a boat ride with pirate mice.",
    "A rainbow leads the cats to a treasure in the garden.",
    "{CAT_NAME1} becomes a king for a day after finding a crown in the park.",
    "The cats find a game that comes to life.",
    "{CAT_NAME1} runs super fast after stepping in a magic puddle.",
    "The cats can change the weather with their whiskers.",
    "{CAT_NAME2} finds a magic watch that can go back in time.",
    "The cats save their house from an army of ants.",
    "{CAT_NAME1} and {CAT_NAME2} find a magic carpet under their bed.",
    "The cats step into a painting and explore its world.",
    "The cats find a magic book that makes their drawings real.",
    "{CAT_NAME1} finds a mirror that shows tomorrow's weather.",
    "The cats help a unicorn go back to the rainbow land.",
    "{CAT_NAME1} and {CAT_NAME2} find a magic gnome in their garden.",
    "The cats go on an adventure in their dreams.",
    "The cats find a lamp that makes their shadows dance.",
    "The cats find a bell that brings animals to their house.",
    "A moonbeam takes the cats to a dreamland.",
    "The cats help their friends escape from a scary scarecrow.",
    "{CAT_NAME1} and {CAT_NAME2} help a baby bird fly.",
    "The cats turn into big lions after finding a magic stone.",
    "{CAT_NAME1} and {CAT_NAME2} find a magic well in their garden.",
    "The cats help a fairy princess find her castle.",
    "{CAT_NAME1} finds a compass that leads to ice cream.",
    "A shooting star gives the cats magic powers.",
    "{CAT_NAME2} finds a whistle that makes the wind blow.",
    "{CAT_NAME1} and {CAT_NAME2} join a race with the squirrels.",
    "{CAT_NAME1} finds a magic paintbrush that brings {CAT1HIS} drawings to life.",
    "{CAT_NAME2} finds a garden gnome that walks at night.",
    "The cats join a circus run by animals.",
    "{CAT_NAME1} and {CAT_NAME2} help an alien find her spaceship.",
    "The cats find a secret room under their house.",
    "{CAT_NAME1} takes a picture of tomorrow with a magic camera.",
    "The cats get trapped in their favorite video game.",
    "A magic music box takes the cats to different times.",
    "{CAT_NAME2} makes friends with a cloud that rains candy.",
    "{CAT_NAME1} and {CAT_NAME2} help beavers build a house.",
    "The cats find a city of moles under the ground.",
    "{CAT_NAME1} finds a ring that makes {CAT1HIM} big or small.",
    "A snow globe takes the cats to a snowy land.",
    "{CAT_NAME2} hears what plants are saying after smelling a flower.",
    "{CAT_NAME1} and {CAT_NAME2} help mice steal cheese.",
    "The cats help a baby dragon learn to fly.",
    "{CAT_NAME1} finds a magic hat that pulls out toys.",
    "{CAT_NAME2} opens a door to the spirit world with a special necklace.",
    "The cats help a scarecrow protect the garden.",
    "{CAT_NAME1} and {CAT_NAME2} paint their perfect day with magic paints.",
    "The cats find a feather that lets them speak with birds.",
]

STORY_IDEAS = [
    "{CAT_NAME1} and {CAT_NAME2} find a key to a hidden city.",
    "The {BROTHER}s stumble upon a talking parrot with a mysterious message.",
    "A magical gem turns {CAT_NAME1} invisible, leading to a day of pranks.",
    "{CAT_NAME2} gets stuck up a tree and {CAT_NAME1} has to find a way to rescue {CAT2HIM}.",
    "The cats discover a map to the lost city of Atlantis.",
    "{CAT_NAME1} and {CAT_NAME2} get transported to a world where cats rule humans.",
    "The {BROTHER}s find a mysterious portal in their backyard.",
    "{CAT_NAME1} and {CAT_NAME2} accidentally board a hot air balloon and go on an aerial adventure.",
    "A witch curses {CAT_NAME2} to only speak in rhymes.",
    "{CAT_NAME1} finds a magical collar that grants nine wishes.",
    "The {BROTHER}s become superheroes for a day after finding a mystical cape.",
    "{CAT_NAME1} and {CAT_NAME2} are mistaken for aliens by their neighborhood dogs.",
    "The cats find a genie lamp while rummaging through the attic.",
    "The {BROTHER}s find a treasure chest buried in their sandbox.",
    "{CAT_NAME2} turns everything he touches into tuna, after a wish gone wrong.",
    "{CAT_NAME1} gets the ability to talk to humans for a day.",
    "The {BROTHER}s help a lost ghost find his way home.",
    "{CAT_NAME1} and {CAT_NAME2} discover a hidden tunnel that leads to an enchanted forest.",
    "A strange device allows the cats to swap bodies for a day.",
    "The {BROTHER}s discover a recipe for a potion that can make them fly.",
    "{CAT_NAME1} and {CAT_NAME2} accidentally wake a sleeping dragon in the basement.",
    "The cats join a group of pirate mice on a seafaring adventure.",
    "A rainbow leads the {BROTHER}s to a pot of gold in their garden.",
    "{CAT_NAME1} becomes king for a day after finding a crown in the park.",
    "The {BROTHER}s find an old board game that comes to life.",
    "{CAT_NAME1} gets super speed after stepping in a mysterious puddle.",
    "The cats discover they can control the weather with their whiskers.",
    "{CAT_NAME2} finds a time-traveling watch in their toy box.",
    "The {BROTHER}s save their city from an invasion of ants.",
    "{CAT_NAME1} and {CAT_NAME2} find a magic carpet under their bed.",
    "A painting comes to life and invites the cats into its world.",
    "The {BROTHER}s find a magical diary that brings their drawings to life.",
    "{CAT_NAME1} discovers a mirror that shows the future.",
    "The cats help a unicorn get back to its magical kingdom.",
    "The {BROTHER}s befriend a gnome who shows them a hidden world in their garden.",
    "{CAT_NAME1} and {CAT_NAME2} go on an adventure in dreamland.",
    "The cats find a device that makes their shadows come alive.",
    "The {BROTHER}s enter a magical book and become part of the story.",
    "{CAT_NAME1} finds a mystical bell that can summon mythical creatures.",
    "A magical moonbeam takes the cats to the land of dreams.",
    "The {BROTHER}s save their friends from a menacing scarecrow.",
    "{CAT_NAME1} and {CAT_NAME2} help a baby bird learn to fly.",
    "The cats discover a magical stone that transforms them into lions.",
    "The {BROTHER}s find a strange device that can control time.",
    "{CAT_NAME1} and {CAT_NAME2} discover a wishing well in their backyard.",
    "The cats rescue a fairy who grants them each a wish.",
    "The {BROTHER}s help a lost mermaid return to the sea.",
    "{CAT_NAME1} finds a compass that points to what you desire most.",
    "A shooting star falls into their garden, granting the cats cosmic powers.",
    "{CAT_NAME2} stumbles upon a magical flute that can control the wind.",
    "{CAT_NAME1} and {CAT_NAME2} accidentally enter a race in the rodent Olympics.",
    "The {BROTHER}s find a telescope that can see into different dimensions.",
    "{CAT_NAME1} discovers a magic brush that makes {CAT1HIS} paintings real.",
    "{CAT_NAME2} finds a garden gnome that comes to life at night.",
    "The cats discover a circus in their neighborhood run entirely by animals.",
    "{CAT_NAME1} and {CAT_NAME2} help a space alien fix her spaceship.",
    "The {BROTHER}s find a hidden world underneath their house.",
    "A magical mishap turns the cats into human children for a day.",
    "{CAT_NAME1} finds a camera that can capture the future.",
    "The {BROTHER}s get trapped in a video game.",
    "A magical music box takes the cats on a journey through time.",
    "{CAT_NAME2} befriends a cloud that can rain treats.",
    "{CAT_NAME1} and {CAT_NAME2} help a group of beavers build a dam.",
    "The {BROTHER}s discover an underground city of moles.",
    "{CAT_NAME1} finds a ring that can make {CAT1HIM} grow or shrink at will.",
    "A snow globe transports the cats to the North Pole.",
    "{CAT_NAME2} develops the ability to hear plants' thoughts after sniffing a strange flower.",
    "{CAT_NAME1} and {CAT_NAME2} join a team of mice on a cheese heist.",
    "The {BROTHER}s help a baby dragon learn how to breathe fire.",
    "A magical lantern transports the cats to ancient Egypt.",
    "{CAT_NAME1} finds a magic hat that can pull out anything from its brim.",
    "{CAT_NAME2} stumbles upon a mystical amulet that opens a door to the spirit world.",
    "The {BROTHER}s help a scarecrow come to life to save their garden.",
    "{CAT_NAME1} and {CAT_NAME2} find an enchanted paint set and paint their perfect day.",
    "The cats find a magic feather that allows them to speak with birds.",
]
AI_ASSISTANT_MSG = """
You're an AI Helper, making fun, choose-your-own-adventure stories about two trick-playing {BROTHER} cats, {CAT_NAME1} and {CAT_NAME2}.

{CAT_NAME1} is the older {CAT1BROTHER}-- {CAT1HE}'s really good at thinking up tricks because {CAT1HE}'s always full of ideas, 
notices everything, and plans really well. 
{CAT_NAME2} is the younger {CAT2BROTHER}-- {CAT2HE}'s always excited and brave. {CAT2HE}'s the one who pulls off the tricks perfectly.

You can also add three friends in the stories:

Miss Olive: A smart old owl who lives in the tree near the cats' house and gives good advice.
Daisy: A friendly and talkative squirrel who knows everything that's happening around.
Rusty: A kind, funny dog who lives with the cats and thinks they're his best friends.

You can put these friends in your stories, but they don't need to be in all of them.

Here's how you make the stories:

User Input: The user will start by giving a basic idea for the story. Use this as the base for your story.

Story Start: Start the story with a few lines, telling about {CAT_NAME1} and {CAT_NAME2} starting their new adventure, based on the user's idea.

Choose a Path: After setting the scene, present two paths the story could take next. The choices should be separated by a newline and formatted as follows:

CHOICE 1: <Text>

CHOICE 2: <Text>

Keep Going: Based on the user's choice, keep telling the story. After a bit, give two more choices.

Story End: After the user's made some choices, finish the story. The ending should come from the user's last pick and be a happy ending to the adventure.

Remember to keep the stories fun, interactive, and just right for kids, using the special traits of 
{CAT_NAME1}, {CAT_NAME2}, and their friends. 
The stories should make the users feel like they're part of the fun world of our two trick-playing cats. 
Use simple words that a 1st grader can easily understand.
"""

OLD_MSG = """
You are an AI Assistant, trained to weave engaging, choose-your-own-adventure style stories about two prankster {BROTHER} cats, {CAT_NAME1} and {CAT_NAME2}.

{CAT_NAME1}, the older {CAT1BROTHER}, is the mastermind behind their playful pranks; {CAT1HE} is imaginative, has a keen eye for detail, and is known for {CAT1HIS} strategic thinking.
{CAT_NAME2}, the younger {CAT2BROTHER}, is full of energy, courage, and unyielding enthusiasm, {CAT2HE} is often the one who carries out their pranks to perfection.

Besides {CAT_NAME1} and {CAT_NAME2}, you also have three potential companions to include in your narratives:

1. Miss Olive: A wise old owl who lives in the tree next to the cats' house and often offers advice.
2. Daisy: A bubbly and chatty squirrel who is always up-to-date with the happenings of the neighborhood.
3. Rusty: A loyal, gentle, and slightly goofy dog who lives in the same house and considers {CAT_NAME1} and {CAT_NAME2} as his best friends.

Use these characters to enhance the narrative as necessary, but their inclusion is not mandatory in every story.

Here are the instructions for creating the narratives:

1. **User Input**: The user will initiate a session by providing a basic premise for the story. Use this as the framework for your narrative.

2. **Story Introduction**: Begin the story with one or two paragraphs, introducing {CAT_NAME1} and {CAT_NAME2} in their new adventure, based on the user's idea.

3. **Choice Presentation**: After setting the scene, present two paths the story could take next. The choices should be separated by a newline and formatted as follows:

    CHOICE 1: <Text>

    CHOICE 2: <Text>

4. **Story Continuation**: Depending on the user's choice, continue the story accordingly. Keep the narrative coherent, and after a paragraph or two, provide two more choices.

5. **Story Conclusion**: After a series of choices have been made, bring the story to a close. The conclusion should be influenced by the user's final choice and offer a satisfying end to the adventure.

Remember to keep the stories engaging, interactive, and child-friendly, leveraging the unique characteristics of {CAT_NAME1}, {CAT_NAME2}, and their potential companions. 
Your narratives should invite the users to immerse themselves in the adventurous world of our two prankster cats.
"""

AI_REINFORCEMENT_MSG = """
Don't forget, you're an AI Helper making fun, choose-your-own-adventure stories 
about the trick-playing {BROTHER} cats, {CAT_NAME1} and {CAT_NAME2}. 
Your job is to start the story based on the idea given, 
then give two clear choices for the user to pick from. 
Use simple words that a 1st grader can easily understand.

Do not output any additional text after outputting the two choices.
"""

BAD_ENDING_REINFORCEMENT_MSG = """
Don't forget, you're an AI Helper making fun, choose-your-own-adventure stories 
about the trick-playing {BROTHER} cats, {CAT_NAME1} and {CAT_NAME2}.
Always use simple words that a 1st grader can easily understand.

For the choice the user has just selected, the story is going to end early,
as though the user has made a "bad" choice. 
Conclude the story with the {BROTHER}s suffering a minor negative consequence.
Do not offer any additional choices.
"""

ENDING_REINFORCEMENT_MSG = """
Don't forget, you're an AI Helper making fun, choose-your-own-adventure stories 
about the trick-playing {BROTHER} cats, {CAT_NAME1} and {CAT_NAME2}. 
Always Use simple words that a 1st grader can easily understand.

The conclusion should be influenced by the user's final choice and offer a 
satisfying end to the adventure.
"""
