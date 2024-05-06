from abc import ABCMeta 
import numpy as np 

class Pokemon(metaclass=ABCMeta):

    Types={'Steel': 0, 'Fighting': 1, 'Dragon': 2, 'Water': 3, 'Fire': 4, 'Electrik': 5, 'Fairy': 6, 'Ice': 7, 'Bug': 8, 'Normal': 9, 'Grass': 10, 'Poison': 11, 'Psychic': 12, 'Ground': 13, 'Rock': 14, 'Ghost': 15, 'Darness': 16, 'Flying': 17}

    Affinites = np.genfromtxt ('../data/Donnees_crees/Affinites.csv', delimiter =';',skip_header=1,usecols=range(1,19))

    def __init__(self, ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary ):
        self.ID=ID
        self.nom=nom
        self.type1=type1 
        self.type2=type2 
        self.Total= Total 
        self.HP=  HP
        self.Attack= Attack 
        self.Defense= Defense 
        self.Sp_Atk= Sp_Atk 
        self.Sp_Def= Sp_Def 
        self.Speed= Speed 
        self.Generation= Generation 
        self.Legendary= Legendary 


class Bulbasaur (Pokemon):
    def __init__(self, ID ='1',nom='Bulbasaur', type1='Grass', type2='Poison', Total=318,HP=45, Attack=49, Defense=49, Sp_Atk=65, Sp_Def=65, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Ivysaur (Pokemon):
    def __init__(self, ID ='2',nom='Ivysaur', type1='Grass', type2='Poison', Total=405,HP=60, Attack=62, Defense=63, Sp_Atk=80, Sp_Def=80, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Venusaur (Pokemon):
    def __init__(self, ID ='3',nom='Venusaur', type1='Grass', type2='Poison', Total=525,HP=80, Attack=82, Defense=83, Sp_Atk=100, Sp_Def=100, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Charmander (Pokemon):
    def __init__(self, ID ='4',nom='Charmander', type1='Fire', type2='null', Total=309,HP=39, Attack=52, Defense=43, Sp_Atk=60, Sp_Def=50, Speed=65, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Charmeleon (Pokemon):
    def __init__(self, ID ='5',nom='Charmeleon', type1='Fire', type2='null', Total=405,HP=58, Attack=64, Defense=58, Sp_Atk=80, Sp_Def=65, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Charizard (Pokemon):
    def __init__(self, ID ='6',nom='Charizard', type1='Fire', type2='Flying', Total=534,HP=78, Attack=84, Defense=78, Sp_Atk=109, Sp_Def=85, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Squirtle (Pokemon):
    def __init__(self, ID ='7',nom='Squirtle', type1='Water', type2='null', Total=314,HP=44, Attack=48, Defense=65, Sp_Atk=50, Sp_Def=64, Speed=43, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Wartortle (Pokemon):
    def __init__(self, ID ='8',nom='Wartortle', type1='Water', type2='null', Total=405,HP=59, Attack=63, Defense=80, Sp_Atk=65, Sp_Def=80, Speed=58, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Blastoise (Pokemon):
    def __init__(self, ID ='9',nom='Blastoise', type1='Water', type2='null', Total=530,HP=79, Attack=83, Defense=100, Sp_Atk=85, Sp_Def=105, Speed=78, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Caterpie (Pokemon):
    def __init__(self, ID ='10',nom='Caterpie', type1='Bug', type2='null', Total=195,HP=45, Attack=30, Defense=35, Sp_Atk=20, Sp_Def=20, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Metapod (Pokemon):
    def __init__(self, ID ='11',nom='Metapod', type1='Bug', type2='null', Total=205,HP=50, Attack=20, Defense=55, Sp_Atk=25, Sp_Def=25, Speed=30, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Butterfree (Pokemon):
    def __init__(self, ID ='12',nom='Butterfree', type1='Bug', type2='Flying', Total=395,HP=60, Attack=45, Defense=50, Sp_Atk=90, Sp_Def=80, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Weedle (Pokemon):
    def __init__(self, ID ='13',nom='Weedle', type1='Bug', type2='Poison', Total=195,HP=40, Attack=35, Defense=30, Sp_Atk=20, Sp_Def=20, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Kakuna (Pokemon):
    def __init__(self, ID ='14',nom='Kakuna', type1='Bug', type2='Poison', Total=205,HP=45, Attack=25, Defense=50, Sp_Atk=25, Sp_Def=25, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Beedrill (Pokemon):
    def __init__(self, ID ='15',nom='Beedrill', type1='Bug', type2='Poison', Total=395,HP=65, Attack=90, Defense=40, Sp_Atk=45, Sp_Def=80, Speed=75, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Pidgey (Pokemon):
    def __init__(self, ID ='16',nom='Pidgey', type1='Normal', type2='Flying', Total=251,HP=40, Attack=45, Defense=40, Sp_Atk=35, Sp_Def=35, Speed=56, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Pidgeotto (Pokemon):
    def __init__(self, ID ='17',nom='Pidgeotto', type1='Normal', type2='Flying', Total=349,HP=63, Attack=60, Defense=55, Sp_Atk=50, Sp_Def=50, Speed=71, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Pidgeot (Pokemon):
    def __init__(self, ID ='18',nom='Pidgeot', type1='Normal', type2='Flying', Total=479,HP=83, Attack=80, Defense=75, Sp_Atk=70, Sp_Def=70, Speed=101, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Rattata (Pokemon):
    def __init__(self, ID ='19',nom='Rattata', type1='Normal', type2='null', Total=253,HP=30, Attack=56, Defense=35, Sp_Atk=25, Sp_Def=35, Speed=72, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Raticate (Pokemon):
    def __init__(self, ID ='20',nom='Raticate', type1='Normal', type2='null', Total=413,HP=55, Attack=81, Defense=60, Sp_Atk=50, Sp_Def=70, Speed=97, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Spearow (Pokemon):
    def __init__(self, ID ='21',nom='Spearow', type1='Normal', type2='Flying', Total=262,HP=40, Attack=60, Defense=30, Sp_Atk=31, Sp_Def=31, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Fearow (Pokemon):
    def __init__(self, ID ='22',nom='Fearow', type1='Normal', type2='Flying', Total=442,HP=65, Attack=90, Defense=65, Sp_Atk=61, Sp_Def=61, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Ekans (Pokemon):
    def __init__(self, ID ='23',nom='Ekans', type1='Poison', type2='null', Total=288,HP=35, Attack=60, Defense=44, Sp_Atk=40, Sp_Def=54, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Arbok (Pokemon):
    def __init__(self, ID ='24',nom='Arbok', type1='Poison', type2='null', Total=438,HP=60, Attack=85, Defense=69, Sp_Atk=65, Sp_Def=79, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Pikachu (Pokemon):
    def __init__(self, ID ='25',nom='Pikachu', type1='Electric', type2='null', Total=320,HP=35, Attack=55, Defense=40, Sp_Atk=50, Sp_Def=50, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Raichu (Pokemon):
    def __init__(self, ID ='26',nom='Raichu', type1='Electric', type2='null', Total=485,HP=60, Attack=90, Defense=55, Sp_Atk=90, Sp_Def=80, Speed=110, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Sandshrew (Pokemon):
    def __init__(self, ID ='27',nom='Sandshrew', type1='Ground', type2='null', Total=300,HP=50, Attack=75, Defense=85, Sp_Atk=20, Sp_Def=30, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Sandslash (Pokemon):
    def __init__(self, ID ='28',nom='Sandslash', type1='Ground', type2='null', Total=450,HP=75, Attack=100, Defense=110, Sp_Atk=45, Sp_Def=55, Speed=65, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Nidoran_male (Pokemon):
    def __init__(self, ID ='29',nom='Nidoran_male', type1='Poison', type2='null', Total=275,HP=55, Attack=47, Defense=52, Sp_Atk=40, Sp_Def=40, Speed=41, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Nidorina (Pokemon):
    def __init__(self, ID ='30',nom='Nidorina', type1='Poison', type2='null', Total=365,HP=70, Attack=62, Defense=67, Sp_Atk=55, Sp_Def=55, Speed=56, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Nidoqueen (Pokemon):
    def __init__(self, ID ='31',nom='Nidoqueen', type1='Poison', type2='Ground', Total=505,HP=90, Attack=92, Defense=87, Sp_Atk=75, Sp_Def=85, Speed=76, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Nidoran_female (Pokemon):
    def __init__(self, ID ='32',nom='Nidoran_female', type1='Poison', type2='null', Total=273,HP=46, Attack=57, Defense=40, Sp_Atk=40, Sp_Def=40, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Nidorino (Pokemon):
    def __init__(self, ID ='33',nom='Nidorino', type1='Poison', type2='null', Total=365,HP=61, Attack=72, Defense=57, Sp_Atk=55, Sp_Def=55, Speed=65, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Nidoking (Pokemon):
    def __init__(self, ID ='34',nom='Nidoking', type1='Poison', type2='Ground', Total=505,HP=81, Attack=102, Defense=77, Sp_Atk=85, Sp_Def=75, Speed=85, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Clefairy (Pokemon):
    def __init__(self, ID ='35',nom='Clefairy', type1='Fairy', type2='null', Total=323,HP=70, Attack=45, Defense=48, Sp_Atk=60, Sp_Def=65, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Clefable (Pokemon):
    def __init__(self, ID ='36',nom='Clefable', type1='Fairy', type2='null', Total=483,HP=95, Attack=70, Defense=73, Sp_Atk=95, Sp_Def=90, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Vulpix (Pokemon):
    def __init__(self, ID ='37',nom='Vulpix', type1='Fire', type2='null', Total=299,HP=38, Attack=41, Defense=40, Sp_Atk=50, Sp_Def=65, Speed=65, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Ninetales (Pokemon):
    def __init__(self, ID ='38',nom='Ninetales', type1='Fire', type2='null', Total=505,HP=73, Attack=76, Defense=75, Sp_Atk=81, Sp_Def=100, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Jigglypuff (Pokemon):
    def __init__(self, ID ='39',nom='Jigglypuff', type1='Normal', type2='Fairy', Total=270,HP=115, Attack=45, Defense=20, Sp_Atk=45, Sp_Def=25, Speed=20, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Wigglytuff (Pokemon):
    def __init__(self, ID ='40',nom='Wigglytuff', type1='Normal', type2='Fairy', Total=435,HP=140, Attack=70, Defense=45, Sp_Atk=85, Sp_Def=50, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Zubat (Pokemon):
    def __init__(self, ID ='41',nom='Zubat', type1='Poison', type2='Flying', Total=245,HP=40, Attack=45, Defense=35, Sp_Atk=30, Sp_Def=40, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Golbat (Pokemon):
    def __init__(self, ID ='42',nom='Golbat', type1='Poison', type2='Flying', Total=455,HP=75, Attack=80, Defense=70, Sp_Atk=65, Sp_Def=75, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Oddish (Pokemon):
    def __init__(self, ID ='43',nom='Oddish', type1='Grass', type2='Poison', Total=320,HP=45, Attack=50, Defense=55, Sp_Atk=75, Sp_Def=65, Speed=30, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Gloom (Pokemon):
    def __init__(self, ID ='44',nom='Gloom', type1='Grass', type2='Poison', Total=395,HP=60, Attack=65, Defense=70, Sp_Atk=85, Sp_Def=75, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Vileplume (Pokemon):
    def __init__(self, ID ='45',nom='Vileplume', type1='Grass', type2='Poison', Total=490,HP=75, Attack=80, Defense=85, Sp_Atk=110, Sp_Def=90, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Paras (Pokemon):
    def __init__(self, ID ='46',nom='Paras', type1='Bug', type2='Grass', Total=285,HP=35, Attack=70, Defense=55, Sp_Atk=45, Sp_Def=55, Speed=25, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Parasect (Pokemon):
    def __init__(self, ID ='47',nom='Parasect', type1='Bug', type2='Grass', Total=405,HP=60, Attack=95, Defense=80, Sp_Atk=60, Sp_Def=80, Speed=30, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Venonat (Pokemon):
    def __init__(self, ID ='48',nom='Venonat', type1='Bug', type2='Poison', Total=305,HP=60, Attack=55, Defense=50, Sp_Atk=40, Sp_Def=55, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Venomoth (Pokemon):
    def __init__(self, ID ='49',nom='Venomoth', type1='Bug', type2='Poison', Total=450,HP=70, Attack=65, Defense=60, Sp_Atk=90, Sp_Def=75, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Diglett (Pokemon):
    def __init__(self, ID ='50',nom='Diglett', type1='Ground', type2='null', Total=265,HP=10, Attack=55, Defense=25, Sp_Atk=35, Sp_Def=45, Speed=95, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Dugtrio (Pokemon):
    def __init__(self, ID ='51',nom='Dugtrio', type1='Ground', type2='null', Total=405,HP=35, Attack=80, Defense=50, Sp_Atk=50, Sp_Def=70, Speed=120, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Meowth (Pokemon):
    def __init__(self, ID ='52',nom='Meowth', type1='Normal', type2='null', Total=290,HP=40, Attack=45, Defense=35, Sp_Atk=40, Sp_Def=40, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Persian (Pokemon):
    def __init__(self, ID ='53',nom='Persian', type1='Normal', type2='null', Total=440,HP=65, Attack=70, Defense=60, Sp_Atk=65, Sp_Def=65, Speed=115, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Psyduck (Pokemon):
    def __init__(self, ID ='54',nom='Psyduck', type1='Water', type2='null', Total=320,HP=50, Attack=52, Defense=48, Sp_Atk=65, Sp_Def=50, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Golduck (Pokemon):
    def __init__(self, ID ='55',nom='Golduck', type1='Water', type2='null', Total=500,HP=80, Attack=82, Defense=78, Sp_Atk=95, Sp_Def=80, Speed=85, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Mankey (Pokemon):
    def __init__(self, ID ='56',nom='Mankey', type1='Fighting', type2='null', Total=305,HP=40, Attack=80, Defense=35, Sp_Atk=35, Sp_Def=45, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Primeape (Pokemon):
    def __init__(self, ID ='57',nom='Primeape', type1='Fighting', type2='null', Total=455,HP=65, Attack=105, Defense=60, Sp_Atk=60, Sp_Def=70, Speed=95, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Growlithe (Pokemon):
    def __init__(self, ID ='58',nom='Growlithe', type1='Fire', type2='null', Total=350,HP=55, Attack=70, Defense=45, Sp_Atk=70, Sp_Def=50, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Arcanine (Pokemon):
    def __init__(self, ID ='59',nom='Arcanine', type1='Fire', type2='null', Total=555,HP=90, Attack=110, Defense=80, Sp_Atk=100, Sp_Def=80, Speed=95, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Poliwag (Pokemon):
    def __init__(self, ID ='60',nom='Poliwag', type1='Water', type2='null', Total=300,HP=40, Attack=50, Defense=40, Sp_Atk=40, Sp_Def=40, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Poliwhirl (Pokemon):
    def __init__(self, ID ='61',nom='Poliwhirl', type1='Water', type2='null', Total=385,HP=65, Attack=65, Defense=65, Sp_Atk=50, Sp_Def=50, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Poliwrath (Pokemon):
    def __init__(self, ID ='62',nom='Poliwrath', type1='Water', type2='Fighting', Total=510,HP=90, Attack=95, Defense=95, Sp_Atk=70, Sp_Def=90, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Abra (Pokemon):
    def __init__(self, ID ='63',nom='Abra', type1='Psychic', type2='null', Total=310,HP=25, Attack=20, Defense=15, Sp_Atk=105, Sp_Def=55, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Kadabra (Pokemon):
    def __init__(self, ID ='64',nom='Kadabra', type1='Psychic', type2='null', Total=400,HP=40, Attack=35, Defense=30, Sp_Atk=120, Sp_Def=70, Speed=105, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Alakazam (Pokemon):
    def __init__(self, ID ='65',nom='Alakazam', type1='Psychic', type2='null', Total=500,HP=55, Attack=50, Defense=45, Sp_Atk=135, Sp_Def=95, Speed=120, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Machop (Pokemon):
    def __init__(self, ID ='66',nom='Machop', type1='Fighting', type2='null', Total=305,HP=70, Attack=80, Defense=50, Sp_Atk=35, Sp_Def=35, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Machoke (Pokemon):
    def __init__(self, ID ='67',nom='Machoke', type1='Fighting', type2='null', Total=405,HP=80, Attack=100, Defense=70, Sp_Atk=50, Sp_Def=60, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Machamp (Pokemon):
    def __init__(self, ID ='68',nom='Machamp', type1='Fighting', type2='null', Total=505,HP=90, Attack=130, Defense=80, Sp_Atk=65, Sp_Def=85, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Bellsprout (Pokemon):
    def __init__(self, ID ='69',nom='Bellsprout', type1='Grass', type2='Poison', Total=300,HP=50, Attack=75, Defense=35, Sp_Atk=70, Sp_Def=30, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Weepinbell (Pokemon):
    def __init__(self, ID ='70',nom='Weepinbell', type1='Grass', type2='Poison', Total=390,HP=65, Attack=90, Defense=50, Sp_Atk=85, Sp_Def=45, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Victreebel (Pokemon):
    def __init__(self, ID ='71',nom='Victreebel', type1='Grass', type2='Poison', Total=490,HP=80, Attack=105, Defense=65, Sp_Atk=100, Sp_Def=70, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Tentacool (Pokemon):
    def __init__(self, ID ='72',nom='Tentacool', type1='Water', type2='Poison', Total=335,HP=40, Attack=40, Defense=35, Sp_Atk=50, Sp_Def=100, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Tentacruel (Pokemon):
    def __init__(self, ID ='73',nom='Tentacruel', type1='Water', type2='Poison', Total=515,HP=80, Attack=70, Defense=65, Sp_Atk=80, Sp_Def=120, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Geodude (Pokemon):
    def __init__(self, ID ='74',nom='Geodude', type1='Rock', type2='Ground', Total=300,HP=40, Attack=80, Defense=100, Sp_Atk=30, Sp_Def=30, Speed=20, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Graveler (Pokemon):
    def __init__(self, ID ='75',nom='Graveler', type1='Rock', type2='Ground', Total=390,HP=55, Attack=95, Defense=115, Sp_Atk=45, Sp_Def=45, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Golem (Pokemon):
    def __init__(self, ID ='76',nom='Golem', type1='Rock', type2='Ground', Total=495,HP=80, Attack=120, Defense=130, Sp_Atk=55, Sp_Def=65, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Ponyta (Pokemon):
    def __init__(self, ID ='77',nom='Ponyta', type1='Fire', type2='null', Total=410,HP=50, Attack=85, Defense=55, Sp_Atk=65, Sp_Def=65, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Rapidash (Pokemon):
    def __init__(self, ID ='78',nom='Rapidash', type1='Fire', type2='null', Total=500,HP=65, Attack=100, Defense=70, Sp_Atk=80, Sp_Def=80, Speed=105, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Slowpoke (Pokemon):
    def __init__(self, ID ='79',nom='Slowpoke', type1='Water', type2='Psychic', Total=315,HP=90, Attack=65, Defense=65, Sp_Atk=40, Sp_Def=40, Speed=15, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Slowbro (Pokemon):
    def __init__(self, ID ='80',nom='Slowbro', type1='Water', type2='Psychic', Total=490,HP=95, Attack=75, Defense=110, Sp_Atk=100, Sp_Def=80, Speed=30, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Magnemite (Pokemon):
    def __init__(self, ID ='81',nom='Magnemite', type1='Electric', type2='Steel', Total=325,HP=25, Attack=35, Defense=70, Sp_Atk=95, Sp_Def=55, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Magneton (Pokemon):
    def __init__(self, ID ='82',nom='Magneton', type1='Electric', type2='Steel', Total=465,HP=50, Attack=60, Defense=95, Sp_Atk=120, Sp_Def=70, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Farfetchd (Pokemon):
    def __init__(self, ID ='83',nom='Farfetchd', type1='Normal', type2='Flying', Total=352,HP=52, Attack=65, Defense=55, Sp_Atk=58, Sp_Def=62, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Doduo (Pokemon):
    def __init__(self, ID ='84',nom='Doduo', type1='Normal', type2='Flying', Total=310,HP=35, Attack=85, Defense=45, Sp_Atk=35, Sp_Def=35, Speed=75, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Dodrio (Pokemon):
    def __init__(self, ID ='85',nom='Dodrio', type1='Normal', type2='Flying', Total=460,HP=60, Attack=110, Defense=70, Sp_Atk=60, Sp_Def=60, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Seel (Pokemon):
    def __init__(self, ID ='86',nom='Seel', type1='Water', type2='null', Total=325,HP=65, Attack=45, Defense=55, Sp_Atk=45, Sp_Def=70, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Dewgong (Pokemon):
    def __init__(self, ID ='87',nom='Dewgong', type1='Water', type2='Ice', Total=475,HP=90, Attack=70, Defense=80, Sp_Atk=70, Sp_Def=95, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Grimer (Pokemon):
    def __init__(self, ID ='88',nom='Grimer', type1='Poison', type2='null', Total=325,HP=80, Attack=80, Defense=50, Sp_Atk=40, Sp_Def=50, Speed=25, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Muk (Pokemon):
    def __init__(self, ID ='89',nom='Muk', type1='Poison', type2='null', Total=500,HP=105, Attack=105, Defense=75, Sp_Atk=65, Sp_Def=100, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Shellder (Pokemon):
    def __init__(self, ID ='90',nom='Shellder', type1='Water', type2='null', Total=305,HP=30, Attack=65, Defense=100, Sp_Atk=45, Sp_Def=25, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Cloyster (Pokemon):
    def __init__(self, ID ='91',nom='Cloyster', type1='Water', type2='Ice', Total=525,HP=50, Attack=95, Defense=180, Sp_Atk=85, Sp_Def=45, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Gastly (Pokemon):
    def __init__(self, ID ='92',nom='Gastly', type1='Ghost', type2='Poison', Total=310,HP=30, Attack=35, Defense=30, Sp_Atk=100, Sp_Def=35, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Haunter (Pokemon):
    def __init__(self, ID ='93',nom='Haunter', type1='Ghost', type2='Poison', Total=405,HP=45, Attack=50, Defense=45, Sp_Atk=115, Sp_Def=55, Speed=95, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Gengar (Pokemon):
    def __init__(self, ID ='94',nom='Gengar', type1='Ghost', type2='Poison', Total=500,HP=60, Attack=65, Defense=60, Sp_Atk=130, Sp_Def=75, Speed=110, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Onix (Pokemon):
    def __init__(self, ID ='95',nom='Onix', type1='Rock', type2='Ground', Total=385,HP=35, Attack=45, Defense=160, Sp_Atk=30, Sp_Def=45, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Drowzee (Pokemon):
    def __init__(self, ID ='96',nom='Drowzee', type1='Psychic', type2='null', Total=328,HP=60, Attack=48, Defense=45, Sp_Atk=43, Sp_Def=90, Speed=42, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Hypno (Pokemon):
    def __init__(self, ID ='97',nom='Hypno', type1='Psychic', type2='null', Total=483,HP=85, Attack=73, Defense=70, Sp_Atk=73, Sp_Def=115, Speed=67, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Krabby (Pokemon):
    def __init__(self, ID ='98',nom='Krabby', type1='Water', type2='null', Total=325,HP=30, Attack=105, Defense=90, Sp_Atk=25, Sp_Def=25, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Kingler (Pokemon):
    def __init__(self, ID ='99',nom='Kingler', type1='Water', type2='null', Total=475,HP=55, Attack=130, Defense=115, Sp_Atk=50, Sp_Def=50, Speed=75, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Voltorb (Pokemon):
    def __init__(self, ID ='100',nom='Voltorb', type1='Electric', type2='null', Total=330,HP=40, Attack=30, Defense=50, Sp_Atk=55, Sp_Def=55, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Electrode (Pokemon):
    def __init__(self, ID ='101',nom='Electrode', type1='Electric', type2='null', Total=480,HP=60, Attack=50, Defense=70, Sp_Atk=80, Sp_Def=80, Speed=140, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Exeggcute (Pokemon):
    def __init__(self, ID ='102',nom='Exeggcute', type1='Grass', type2='Psychic', Total=325,HP=60, Attack=40, Defense=80, Sp_Atk=60, Sp_Def=45, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Exeggutor (Pokemon):
    def __init__(self, ID ='103',nom='Exeggutor', type1='Grass', type2='Psychic', Total=520,HP=95, Attack=95, Defense=85, Sp_Atk=125, Sp_Def=65, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Cubone (Pokemon):
    def __init__(self, ID ='104',nom='Cubone', type1='Ground', type2='null', Total=320,HP=50, Attack=50, Defense=95, Sp_Atk=40, Sp_Def=50, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Marowak (Pokemon):
    def __init__(self, ID ='105',nom='Marowak', type1='Ground', type2='null', Total=425,HP=60, Attack=80, Defense=110, Sp_Atk=50, Sp_Def=80, Speed=45, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Hitmonlee (Pokemon):
    def __init__(self, ID ='106',nom='Hitmonlee', type1='Fighting', type2='null', Total=455,HP=50, Attack=120, Defense=53, Sp_Atk=35, Sp_Def=110, Speed=87, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Hitmonchan (Pokemon):
    def __init__(self, ID ='107',nom='Hitmonchan', type1='Fighting', type2='null', Total=455,HP=50, Attack=105, Defense=79, Sp_Atk=35, Sp_Def=110, Speed=76, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Lickitung (Pokemon):
    def __init__(self, ID ='108',nom='Lickitung', type1='Normal', type2='null', Total=385,HP=90, Attack=55, Defense=75, Sp_Atk=60, Sp_Def=75, Speed=30, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Koffing (Pokemon):
    def __init__(self, ID ='109',nom='Koffing', type1='Poison', type2='null', Total=340,HP=40, Attack=65, Defense=95, Sp_Atk=60, Sp_Def=45, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Weezing (Pokemon):
    def __init__(self, ID ='110',nom='Weezing', type1='Poison', type2='null', Total=490,HP=65, Attack=90, Defense=120, Sp_Atk=85, Sp_Def=70, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Rhyhorn (Pokemon):
    def __init__(self, ID ='111',nom='Rhyhorn', type1='Ground', type2='Rock', Total=345,HP=80, Attack=85, Defense=95, Sp_Atk=30, Sp_Def=30, Speed=25, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Rhydon (Pokemon):
    def __init__(self, ID ='112',nom='Rhydon', type1='Ground', type2='Rock', Total=485,HP=105, Attack=130, Defense=120, Sp_Atk=45, Sp_Def=45, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Chansey (Pokemon):
    def __init__(self, ID ='113',nom='Chansey', type1='Normal', type2='null', Total=450,HP=250, Attack=5, Defense=5, Sp_Atk=35, Sp_Def=105, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Tangela (Pokemon):
    def __init__(self, ID ='114',nom='Tangela', type1='Grass', type2='null', Total=435,HP=65, Attack=55, Defense=115, Sp_Atk=100, Sp_Def=40, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Kangaskhan (Pokemon):
    def __init__(self, ID ='115',nom='Kangaskhan', type1='Normal', type2='null', Total=490,HP=105, Attack=95, Defense=80, Sp_Atk=40, Sp_Def=80, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Horsea (Pokemon):
    def __init__(self, ID ='116',nom='Horsea', type1='Water', type2='null', Total=295,HP=30, Attack=40, Defense=70, Sp_Atk=70, Sp_Def=25, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Seadra (Pokemon):
    def __init__(self, ID ='117',nom='Seadra', type1='Water', type2='null', Total=440,HP=55, Attack=65, Defense=95, Sp_Atk=95, Sp_Def=45, Speed=85, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Goldeen (Pokemon):
    def __init__(self, ID ='118',nom='Goldeen', type1='Water', type2='null', Total=320,HP=45, Attack=67, Defense=60, Sp_Atk=35, Sp_Def=50, Speed=63, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Seaking (Pokemon):
    def __init__(self, ID ='119',nom='Seaking', type1='Water', type2='null', Total=450,HP=80, Attack=92, Defense=65, Sp_Atk=65, Sp_Def=80, Speed=68, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Staryu (Pokemon):
    def __init__(self, ID ='120',nom='Staryu', type1='Water', type2='null', Total=340,HP=30, Attack=45, Defense=55, Sp_Atk=70, Sp_Def=55, Speed=85, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Starmie (Pokemon):
    def __init__(self, ID ='121',nom='Starmie', type1='Water', type2='Psychic', Total=520,HP=60, Attack=75, Defense=85, Sp_Atk=100, Sp_Def=85, Speed=115, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Mr_Mime (Pokemon):
    def __init__(self, ID ='122',nom='Mr_Mime', type1='Psychic', type2='Fairy', Total=460,HP=40, Attack=45, Defense=65, Sp_Atk=100, Sp_Def=120, Speed=90, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Scyther (Pokemon):
    def __init__(self, ID ='123',nom='Scyther', type1='Bug', type2='Flying', Total=500,HP=70, Attack=110, Defense=80, Sp_Atk=55, Sp_Def=80, Speed=105, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Jynx (Pokemon):
    def __init__(self, ID ='124',nom='Jynx', type1='Ice', type2='Psychic', Total=455,HP=65, Attack=50, Defense=35, Sp_Atk=115, Sp_Def=95, Speed=95, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Electabuzz (Pokemon):
    def __init__(self, ID ='125',nom='Electabuzz', type1='Electric', type2='null', Total=490,HP=65, Attack=83, Defense=57, Sp_Atk=95, Sp_Def=85, Speed=105, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Magmar (Pokemon):
    def __init__(self, ID ='126',nom='Magmar', type1='Fire', type2='null', Total=495,HP=65, Attack=95, Defense=57, Sp_Atk=100, Sp_Def=85, Speed=93, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Pinsir (Pokemon):
    def __init__(self, ID ='127',nom='Pinsir', type1='Bug', type2='null', Total=500,HP=65, Attack=125, Defense=100, Sp_Atk=55, Sp_Def=70, Speed=85, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Tauros (Pokemon):
    def __init__(self, ID ='128',nom='Tauros', type1='Normal', type2='null', Total=490,HP=75, Attack=100, Defense=95, Sp_Atk=40, Sp_Def=70, Speed=110, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Magikarp (Pokemon):
    def __init__(self, ID ='129',nom='Magikarp', type1='Water', type2='null', Total=200,HP=20, Attack=10, Defense=55, Sp_Atk=15, Sp_Def=20, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Gyarados (Pokemon):
    def __init__(self, ID ='130',nom='Gyarados', type1='Water', type2='Flying', Total=540,HP=95, Attack=125, Defense=79, Sp_Atk=60, Sp_Def=100, Speed=81, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Lapras (Pokemon):
    def __init__(self, ID ='131',nom='Lapras', type1='Water', type2='Ice', Total=535,HP=130, Attack=85, Defense=80, Sp_Atk=85, Sp_Def=95, Speed=60, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Ditto (Pokemon):
    def __init__(self, ID ='132',nom='Ditto', type1='Normal', type2='null', Total=288,HP=48, Attack=48, Defense=48, Sp_Atk=48, Sp_Def=48, Speed=48, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Eevee (Pokemon):
    def __init__(self, ID ='133',nom='Eevee', type1='Normal', type2='null', Total=325,HP=55, Attack=55, Defense=50, Sp_Atk=45, Sp_Def=65, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Vaporeon (Pokemon):
    def __init__(self, ID ='134',nom='Vaporeon', type1='Water', type2='null', Total=525,HP=130, Attack=65, Defense=60, Sp_Atk=110, Sp_Def=95, Speed=65, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Jolteon (Pokemon):
    def __init__(self, ID ='135',nom='Jolteon', type1='Electric', type2='null', Total=525,HP=65, Attack=65, Defense=60, Sp_Atk=110, Sp_Def=95, Speed=130, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Flareon (Pokemon):
    def __init__(self, ID ='136',nom='Flareon', type1='Fire', type2='null', Total=525,HP=65, Attack=130, Defense=60, Sp_Atk=95, Sp_Def=110, Speed=65, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Porygon (Pokemon):
    def __init__(self, ID ='137',nom='Porygon', type1='Normal', type2='null', Total=395,HP=65, Attack=60, Defense=70, Sp_Atk=85, Sp_Def=75, Speed=40, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Omanyte (Pokemon):
    def __init__(self, ID ='138',nom='Omanyte', type1='Rock', type2='Water', Total=355,HP=35, Attack=40, Defense=100, Sp_Atk=90, Sp_Def=55, Speed=35, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Omastar (Pokemon):
    def __init__(self, ID ='139',nom='Omastar', type1='Rock', type2='Water', Total=495,HP=70, Attack=60, Defense=125, Sp_Atk=115, Sp_Def=70, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Kabuto (Pokemon):
    def __init__(self, ID ='140',nom='Kabuto', type1='Rock', type2='Water', Total=355,HP=30, Attack=80, Defense=90, Sp_Atk=55, Sp_Def=45, Speed=55, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Kabutops (Pokemon):
    def __init__(self, ID ='141',nom='Kabutops', type1='Rock', type2='Water', Total=495,HP=60, Attack=115, Defense=105, Sp_Atk=65, Sp_Def=70, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Aerodactyl (Pokemon):
    def __init__(self, ID ='142',nom='Aerodactyl', type1='Rock', type2='Flying', Total=515,HP=80, Attack=105, Defense=65, Sp_Atk=60, Sp_Def=75, Speed=130, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Snorlax (Pokemon):
    def __init__(self, ID ='143',nom='Snorlax', type1='Normal', type2='null', Total=540,HP=160, Attack=110, Defense=65, Sp_Atk=65, Sp_Def=110, Speed=30, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Articuno (Pokemon):
    def __init__(self, ID ='144',nom='Articuno', type1='Ice', type2='Flying', Total=580,HP=90, Attack=85, Defense=100, Sp_Atk=95, Sp_Def=125, Speed=85, Generation='1', Legendary=True):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Zapdos (Pokemon):
    def __init__(self, ID ='145',nom='Zapdos', type1='Electric', type2='Flying', Total=580,HP=90, Attack=90, Defense=85, Sp_Atk=125, Sp_Def=90, Speed=100, Generation='1', Legendary=True):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Moltres (Pokemon):
    def __init__(self, ID ='146',nom='Moltres', type1='Fire', type2='Flying', Total=580,HP=90, Attack=100, Defense=90, Sp_Atk=125, Sp_Def=85, Speed=90, Generation='1', Legendary=True):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Dratini (Pokemon):
    def __init__(self, ID ='147',nom='Dratini', type1='Dragon', type2='null', Total=300,HP=41, Attack=64, Defense=45, Sp_Atk=50, Sp_Def=50, Speed=50, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Dragonair (Pokemon):
    def __init__(self, ID ='148',nom='Dragonair', type1='Dragon', type2='null', Total=420,HP=61, Attack=84, Defense=65, Sp_Atk=70, Sp_Def=70, Speed=70, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Dragonite (Pokemon):
    def __init__(self, ID ='149',nom='Dragonite', type1='Dragon', type2='Flying', Total=600,HP=91, Attack=134, Defense=95, Sp_Atk=100, Sp_Def=100, Speed=80, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Mewtwo (Pokemon):
    def __init__(self, ID ='150',nom='Mewtwo', type1='Psychic', type2='null', Total=680,HP=106, Attack=110, Defense=90, Sp_Atk=154, Sp_Def=90, Speed=130, Generation='1', Legendary=True):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

class Mew (Pokemon):
    def __init__(self, ID ='151',nom='Mew', type1='Psychic', type2='null', Total=600,HP=100, Attack=100, Defense=100, Sp_Atk=100, Sp_Def=100, Speed=100, Generation='1', Legendary=False):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )

if __name__=='__main__':

    dict_pokemons={ 'Bulbasaur' : Bulbasaur(), 'Ivysaur' : Ivysaur(), 'Venusaur' : Venusaur(), 'Charmander' : Charmander(), 'Charmeleon' : Charmeleon(), 'Charizard' : Charizard(), 'Squirtle' : Squirtle(), 'Wartortle' : Wartortle(), 'Blastoise' : Blastoise(), 'Caterpie' : Caterpie(), 'Metapod' : Metapod(), 'Butterfree' : Butterfree(), 'Weedle' : Weedle(), 'Kakuna' : Kakuna(), 'Beedrill' : Beedrill(), 'Pidgey' : Pidgey(), 'Pidgeotto' : Pidgeotto(), 'Pidgeot' : Pidgeot(), 'Rattata' : Rattata(), 'Raticate' : Raticate(), 'Spearow' : Spearow(), 'Fearow' : Fearow(), 'Ekans' : Ekans(), 'Arbok' : Arbok(), 'Pikachu' : Pikachu(), 'Raichu' : Raichu(), 'Sandshrew' : Sandshrew(), 'Sandslash' : Sandslash(), 'Nidoran_male' : Nidoran_male(), 'Nidorina' : Nidorina(), 'Nidoqueen' : Nidoqueen(), 'Nidoran_female' : Nidoran_female(), 'Nidorino' : Nidorino(), 'Nidoking' : Nidoking(), 'Clefairy' : Clefairy(), 'Clefable' : Clefable(), 'Vulpix' : Vulpix(), 'Ninetales' : Ninetales(), 'Jigglypuff' : Jigglypuff(), 'Wigglytuff' : Wigglytuff(), 'Zubat' : Zubat(), 'Golbat' : Golbat(), 'Oddish' : Oddish(), 'Gloom' : Gloom(), 'Vileplume' : Vileplume(), 'Paras' : Paras(), 'Parasect' : Parasect(), 'Venonat' : Venonat(), 'Venomoth' : Venomoth(), 'Diglett' : Diglett(), 'Dugtrio' : Dugtrio(), 'Meowth' : Meowth(), 'Persian' : Persian(), 'Psyduck' : Psyduck(), 'Golduck' : Golduck(), 'Mankey' : Mankey(), 'Primeape' : Primeape(), 'Growlithe' : Growlithe(), 'Arcanine' : Arcanine(), 'Poliwag' : Poliwag(), 'Poliwhirl' : Poliwhirl(), 'Poliwrath' : Poliwrath(), 'Abra' : Abra(), 'Kadabra' : Kadabra(), 'Alakazam' : Alakazam(), 'Machop' : Machop(), 'Machoke' : Machoke(), 'Machamp' : Machamp(), 'Bellsprout' : Bellsprout(), 'Weepinbell' : Weepinbell(), 'Victreebel' : Victreebel(), 'Tentacool' : Tentacool(), 'Tentacruel' : Tentacruel(), 'Geodude' : Geodude(), 'Graveler' : Graveler(), 'Golem' : Golem(), 'Ponyta' : Ponyta(), 'Rapidash' : Rapidash(), 'Slowpoke' : Slowpoke(), 'Slowbro' : Slowbro(), 'Magnemite' : Magnemite(), 'Magneton' : Magneton(), 'Farfetchd' : Farfetchd(), 'Doduo' : Doduo(), 'Dodrio' : Dodrio(), 'Seel' : Seel(), 'Dewgong' : Dewgong(), 'Grimer' : Grimer(), 'Muk' : Muk(), 'Shellder' : Shellder(), 'Cloyster' : Cloyster(), 'Gastly' : Gastly(), 'Haunter' : Haunter(), 'Gengar' : Gengar(), 'Onix' : Onix(), 'Drowzee' : Drowzee(), 'Hypno' : Hypno(), 'Krabby' : Krabby(), 'Kingler' : Kingler(), 'Voltorb' : Voltorb(), 'Electrode' : Electrode(), 'Exeggcute' : Exeggcute(), 'Exeggutor' : Exeggutor(), 'Cubone' : Cubone(), 'Marowak' : Marowak(), 'Hitmonlee' : Hitmonlee(), 'Hitmonchan' : Hitmonchan(), 'Lickitung' : Lickitung(), 'Koffing' : Koffing(), 'Weezing' : Weezing(), 'Rhyhorn' : Rhyhorn(), 'Rhydon' : Rhydon(), 'Chansey' : Chansey(), 'Tangela' : Tangela(), 'Kangaskhan' : Kangaskhan(), 'Horsea' : Horsea(), 'Seadra' : Seadra(), 'Goldeen' : Goldeen(), 'Seaking' : Seaking(), 'Staryu' : Staryu(), 'Starmie' : Starmie(), 'Mr_Mime' : Mr_Mime(), 'Scyther' : Scyther(), 'Jynx' : Jynx(), 'Electabuzz' : Electabuzz(), 'Magmar' : Magmar(), 'Pinsir' : Pinsir(), 'Tauros' : Tauros(), 'Magikarp' : Magikarp(), 'Gyarados' : Gyarados(), 'Lapras' : Lapras(), 'Ditto' : Ditto(), 'Eevee' : Eevee(), 'Vaporeon' : Vaporeon(), 'Jolteon' : Jolteon(), 'Flareon' : Flareon(), 'Porygon' : Porygon(), 'Omanyte' : Omanyte(), 'Omastar' : Omastar(), 'Kabuto' : Kabuto(), 'Kabutops' : Kabutops(), 'Aerodactyl' : Aerodactyl(), 'Snorlax' : Snorlax(), 'Articuno' : Articuno(), 'Zapdos' : Zapdos(), 'Moltres' : Moltres(), 'Dratini' : Dratini(), 'Dragonair' : Dragonair(), 'Dragonite' : Dragonite(), 'Mewtwo' : Mewtwo(), 'Mew' : Mew(), }
    ID_pokemons= { '1' : 'Bulbasaur', '2' : 'Ivysaur', '3' : 'Venusaur', '4' : 'Charmander', '5' : 'Charmeleon', '6' : 'Charizard', '7' : 'Squirtle', '8' : 'Wartortle', '9' : 'Blastoise', '10' : 'Caterpie', '11' : 'Metapod', '12' : 'Butterfree', '13' : 'Weedle', '14' : 'Kakuna', '15' : 'Beedrill', '16' : 'Pidgey', '17' : 'Pidgeotto', '18' : 'Pidgeot', '19' : 'Rattata', '20' : 'Raticate', '21' : 'Spearow', '22' : 'Fearow', '23' : 'Ekans', '24' : 'Arbok', '25' : 'Pikachu', '26' : 'Raichu', '27' : 'Sandshrew', '28' : 'Sandslash', '29' : 'Nidoran_male', '30' : 'Nidorina', '31' : 'Nidoqueen', '32' : 'Nidoran_female', '33' : 'Nidorino', '34' : 'Nidoking', '35' : 'Clefairy', '36' : 'Clefable', '37' : 'Vulpix', '38' : 'Ninetales', '39' : 'Jigglypuff', '40' : 'Wigglytuff', '41' : 'Zubat', '42' : 'Golbat', '43' : 'Oddish', '44' : 'Gloom', '45' : 'Vileplume', '46' : 'Paras', '47' : 'Parasect', '48' : 'Venonat', '49' : 'Venomoth', '50' : 'Diglett', '51' : 'Dugtrio', '52' : 'Meowth', '53' : 'Persian', '54' : 'Psyduck', '55' : 'Golduck', '56' : 'Mankey', '57' : 'Primeape', '58' : 'Growlithe', '59' : 'Arcanine', '60' : 'Poliwag', '61' : 'Poliwhirl', '62' : 'Poliwrath', '63' : 'Abra', '64' : 'Kadabra', '65' : 'Alakazam', '66' : 'Machop', '67' : 'Machoke', '68' : 'Machamp', '69' : 'Bellsprout', '70' : 'Weepinbell', '71' : 'Victreebel', '72' : 'Tentacool', '73' : 'Tentacruel', '74' : 'Geodude', '75' : 'Graveler', '76' : 'Golem', '77' : 'Ponyta', '78' : 'Rapidash', '79' : 'Slowpoke', '80' : 'Slowbro', '81' : 'Magnemite', '82' : 'Magneton', '83' : 'Farfetchd', '84' : 'Doduo', '85' : 'Dodrio', '86' : 'Seel', '87' : 'Dewgong', '88' : 'Grimer', '89' : 'Muk', '90' : 'Shellder', '91' : 'Cloyster', '92' : 'Gastly', '93' : 'Haunter', '94' : 'Gengar', '95' : 'Onix', '96' : 'Drowzee', '97' : 'Hypno', '98' : 'Krabby', '99' : 'Kingler', '100' : 'Voltorb', '101' : 'Electrode', '102' : 'Exeggcute', '103' : 'Exeggutor', '104' : 'Cubone', '105' : 'Marowak', '106' : 'Hitmonlee', '107' : 'Hitmonchan', '108' : 'Lickitung', '109' : 'Koffing', '110' : 'Weezing', '111' : 'Rhyhorn', '112' : 'Rhydon', '113' : 'Chansey', '114' : 'Tangela', '115' : 'Kangaskhan', '116' : 'Horsea', '117' : 'Seadra', '118' : 'Goldeen', '119' : 'Seaking', '120' : 'Staryu', '121' : 'Starmie', '122' : 'Mr_Mime', '123' : 'Scyther', '124' : 'Jynx', '125' : 'Electabuzz', '126' : 'Magmar', '127' : 'Pinsir', '128' : 'Tauros', '129' : 'Magikarp', '130' : 'Gyarados', '131' : 'Lapras', '132' : 'Ditto', '133' : 'Eevee', '134' : 'Vaporeon', '135' : 'Jolteon', '136' : 'Flareon', '137' : 'Porygon', '138' : 'Omanyte', '139' : 'Omastar', '140' : 'Kabuto', '141' : 'Kabutops', '142' : 'Aerodactyl', '143' : 'Snorlax', '144' : 'Articuno', '145' : 'Zapdos', '146' : 'Moltres', '147' : 'Dratini', '148' : 'Dragonair', '149' : 'Dragonite', '150' : 'Mewtwo', '151' : 'Mew', }
    pi=Pikachu()
    Mewtou=Mew()
    Drac=Drowzee()