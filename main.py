import random
import time


# Gameover condition:
def gameover():
    print("GAME OVER")
    print("Quitting...")
    time.sleep(2)
    exit()


# Names DB:
names_m = ["Adam", "Abraham", "Anthony", "Anton", "Alan", "Alex", "Alexander", "Charlie", "David", "Ellis", "Felix", "Harry", "Hank", "Ivor", "James", "John", "Johann", "Jonathan", "Jason", "Jackson", "Leo", "Marco", "Mario", "Nigel", "Nathaniel", "Nate", "Oswald", "Philip", "Robert", "Richard", "Thane", "Thomas"]
names_f = ["Anna", "Alyss", "Beatrice", "Carla", "Dalia", "Dina", "Dagny", "Elise", "Felicia", "Gila", "Ingrid", "Iara", "Ivana", "Julia", "Jane", "Kate", "Kat", "Katherine", "Katy", "Laura", "Lauren", "Lana", "Maria", "Mary", "Mary Ann", "Nadia", "Nadine", "Nicole", "Natasha", "Nathalia", "Pietra", "Rachel", "Raquel", "Sadie", "Tamara", "Veronica", "Vanessa"]
surnames = ["Ackton", "Afton", "Adastra", "Bigwood", "Bedford", "Belford", "Basketon", "Clevland", "Clintonwood", "Cristalion", "Danneford", "Danneskjold", "Eston", "Eldon", "Firewood", "Foxtrom", "Foxskin", "Girdam", "Gator", "Holsford", "Hadamwood", "Isoford", "Iltrom", "Jackson", "Jackwood", "Kinwood", "Kortold", "Lannyard", "Longwood", "Louisington", "Marcowood", "McDonald", "McWood", "McJohnson", "Norville", "Orson", "Pager", "Rearden", "Richardson", "Songbird", "Saxonwood", "Thompson", "Treekin", "Wyatt", "Wellinghton", "Wedge", "Ostrowski", "Da Cunha", "Glanzner", "Taggart"]
codenames = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Julliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]


# Storygen DB:
locations_easy = ["the neighborhood", "the suburbs", "the downtown", "a village", "the streets", "a store"]
locations_avg = ["a multinational", "a tech company", "an advanced factory", "a town hall", "a police station"]
locations_pro = ["the oval office", "the capitol", "the UNO HQ", "a nuclear silo"]
occupations_low = ["a labourer", "a doctor", "a nurse", "a mechanic", "a teacher", "a lawyer"]
occupations_high = ["a MP", "The President", "a Diplomatic Delegate", "a CEO", "a Big Tech Owner", "a Supreme Court Judge"]
mission_types = ["Rescue", "Defense", "Bomb defusal", "Raid"]


# Classes:
class Bystander:
    def __init__(self, name, occupation, gender, lives):
        self.name = name
        self.occupation = occupation
        self.gender = gender
        self.lives = lives

    def get_pronouns(self):
        if self.gender == "m":
            return ["he", "him", "his"]
        elif self.gender == "f":
            return ["she", "her", "hers"]


class Operative:
    def __init__(self, name, rank, gender):
        self.name = name
        self.rank = rank
        self.lives = True
        self.gender = gender
        self.cost = 0
        self.special = "Operator"

    def get_pronouns(self):
        if self.gender == "m":
            return ["he", "him", "his"]
        elif self.gender == "f":
            return ["she", "her", "hers"]

    def get_rank_name(self):
        rank_dic = {0: "Recruit", 1: "Soldier", 2: "Sergeant", 3: "Liutenant", 4: "Captain", 5: "Major", 6: "Colonel", 7: "Commander", 8: "General", 9: "Marshall"}
        return rank_dic[self.rank]

    def set_special(self, newset):
        self.special = newset


class Squad:
    def __init__(self, ccapital):
        self.ccapital = ccapital
        self.operatives = []
        self.diff = 1

    def hire_operative(self, operative):
        if operative.cost > self.ccapital:
            print("You do not have enough corporate capital!")
            return False
        else:
            if len(self.operatives) == len(codenames):
                print("Your team is full!")
                return False
            else:
                self.ccapital = self.ccapital - operative.cost
                self.operatives.append(operative)
                for codename in codenames:
                    if codename not in [o.codename for o in self.operatives]:
                        codename = chosen
                        break
                operative.codename = chosen

    
    def fire_operative(self, operative):
        if operative in self.operatives:
            self.operatives.remove(operative)
        else:
            return False

    def get_leader(self):
        ranks = []
        for r in self.operatives:
            ranks.append(r.rank)
        greatest_rank = max(ranks)
        for ops in self.operatives:
            if ops.rank == greatest_rank:
                return ops

    def ccgain(self, x):
        self.ccapital += x
        if self.diff < 3:
            diff_wg = 10 * x
            conseq = random.choices(["increase", "maintain"], weights = (diff_wg, 100), k = 2)
            if conseq == "increase":
                self.diff += 1


class PMC:
    def __init__(self, name, ceo, wealth):
        self.name = name
        self.ceo = ceo
        self.wealth = wealth


class Faction:
    def __init__(self, name, goons, threat):
        self.name = name
        self.goons = goons
        self.threat = threat


class Mission:
    def __init__(self, type):
        self.type = type

    def begin(self, squad, encounter):
        pprpt_facs = [a for a in enemy_factions if a.threat == squad.diff]
        fac = random.choice(pprpt_facs)
        mssn_diff = squad.diff * random.choice([1,2,3,4])
        success = random.choice(range(-1, squad.get_leader().rank + 1)) >= mssn_diff
        if self.type == ("Rescue" or "Defense"):
            print(f"\n The mission assignment is the following:\nMission type: {self.type}\nTarget: {random.choice(random.choice([occupations_low, occupations_high]))} called {random.choice(random.choice([names_m, names_f]))} {random.choice(surnames)}\nHostiles are from faction: {fac.name}")
            input("Press enter to continue")
        else:
            print(f"The mission assignment is the following:\nMission type: {self.type}\nHostiles are from faction: {fac.name}")
            input("Press enter to continue")

        if success:
            print("The mission was accomplished without incident")
            squad.ccgain(1)
        else:
            combat_sys(squad.operatives, encounter)

# Init Store:
store = [Operative("Thane Silver", 0, "m"), Operative("Rachel Wedge", 0, "f"), Operative("Johann Finger", 1, "m")]


# Functions:
def store_fill():
    while len(store) < 3:
        is_masc = random.choice([True, False])
        rank = random.choice([0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4])
        if is_masc is True:
            store.append(Operative(f"{random.choice(names_m)} {random.choice(surnames)}", rank, "m"))
        else:
            store.append(Operative(f"{random.choice(names_m)} {random.choice(surnames)}", rank, "f"))


# Starter Config:
starter_squad_members = [Operative("James Blade", 3, "m"), Operative("John Ismail", 1, "m"), Operative("Ryan Magnus", 2, "m")]
starter_squad_members[0].codename = "Atlas"
starter_squad_members[1].codename = "Seller"
starter_squad_members[2].codename = "Magnum"
company = PMC("Ares", "Richard Lernen", 1)
squad = Squad(0)
squad.operatives = starter_squad_members


# Factions API:
enemy_factions = [
    Faction("Bandits",
            [Operative("Goon", 0, "m"),
             Operative("Assaulter", 1, "m"),
             Operative("Assault Leader", 2, "m")],
            1),

    Faction("Looter Horde",
            [Operative("Common Looter", 0, "m"),
             Operative("Armed Looter", 1, "m"),
             Operative("Looter Warlord", 3, "m")],
            2),

    Faction("Terrorist Team",
            [Operative("Terrorist Soldier", 1, "m"),
             Operative("Terrorist Captain", 4, "m"),
             Operative("Terrorist Commander", 7, "m")],
            3)
]


# Targetting system:
def target_sys(attacker, target):
    atk_rolls = list(range(-1, attacker.rank + 1))
    if attacker.special == "Ranger":
        atk_rolls.remove(-1)
        atk_rolls.append(attacker.rank)
    def_rolls = list(range(-1, target.rank + 1))
    if target.special == "Armored":
        for r in def_rolls:
            if r != -1:
                r += 2
    atk_die = random.choice(atk_rolls)
    def_die = random.choice(def_rolls)
    if atk_die > def_die:
        target.lives = False


# Combat system:
def combat_sys(friendlies, hostiles):
    participants = friendlies + hostiles
    combat_order = []
    for i in range(0, len(participants)):
        x = random.choice(participants)
        combat_order.append(x)
        participants.remove(x)
    combat = True
    while combat is True:
        for turn in combat_order:
            if turn in friendlies:
                if turn.special == ("Operator" or "Armored"):
                    target = min(hostiles, key=lambda x: x.rank)
                else:
                    target = max(hostiles, key=lambda x: x.rank)
            else:
                target = random.choice(friendlies)
            target_sys(turn, target)
            if target.lives is False:
                combat_order.remove(target)
                if target in friendlies:
                    friendlies.remove(target)
            if friendlies is []:
                gameover()
            if hostiles is []:
                combat = False
                break


# Def menu:
def menu():
    print("Choose your action:")
