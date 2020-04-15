from app import db
from models import *

# Rebuild DB
db.drop_all()
db.create_all()

payload = {
	'email': 'fake@mail.com',
	'password': 'password'
}

jomah = UserModel(payload=payload)
db.session.add(jomah)

# Shelves
already_read = ShelfModel(
	type='already_read',
	user=jomah
)
db.session.add(already_read)

to_read = ShelfModel(
	type='to_read',
	user=jomah
)
db.session.add(to_read)


# Authors
grrm = AuthorModel(name='George R. R. Martin')
db.session.add(grrm)

simpson = AuthorModel(name='Joe Simpson')
db.session.add(simpson)

krakauer = AuthorModel(name='Jon Krakauer')
db.session.add(krakauer)

orwell = AuthorModel(name='George Orwell')
db.session.add(orwell)

vonnegut = AuthorModel(name='Kurt Vonnegut')
db.session.add(vonnegut)

wilde = AuthorModel(name='Oscar Wilde')
db.session.add(wilde)


# Genres
fiction = GenreModel(type='fiction')
db.session.add(fiction)

non_fiction = GenreModel(type='non-fiction')
db.session.add(non_fiction)

fantasy = GenreModel(type='fantasy')
db.session.add(fantasy)

adventure = GenreModel(type='adventure')
db.session.add(adventure)

dystopian = GenreModel(type='dystopian')
db.session.add(dystopian)

science_fiction = GenreModel(type='science_fiction')
db.session.add(science_fiction)

satire = GenreModel(type='satire')
db.session.add(satire)


# Jomah's Books
book1 = BookModel(
	title='A Game of Thrones',
	summary='Winter is coming. Such is the stern motto of House Stark, the northernmost of the fiefdoms that owe allegiance to King Robert Baratheon in far-off King’s Landing. There Eddard Stark of Winterfell rules in Robert’s name. There his family dwells in peace and comfort: his proud wife, Catelyn; his sons Robb, Brandon, and Rickon; his daughters Sansa and Arya; and his bastard son, Jon Snow. Far to the north, behind the towering Wall, lie savage Wildings and worse—unnatural things relegated to myth during the centuries-long summer, but proving all too real and all too deadly in the turning of the season.',
	published_date='1996',
	image_url='https://images-na.ssl-images-amazon.com/images/I/91dSMhdIzTL.jpg',
	isbn='0553103547',
	authors=[grrm],
	genres=[fiction, fantasy],
	shelves=[already_read]
)
db.session.add(book1)

book2 = BookModel(
	title='A Clash of Kings',
	summary='A comet the color of blood and flame cuts across the sky. And from the ancient citadel of Dragonstone to the forbidding shores of Winterfell, chaos reigns. Six factions struggle for control of a divided land and the Iron Throne of the Seven Kingdoms, preparing to stake their claims through tempest, turmoil, and war. It is a tale in which brother plots against brother and the dead rise to walk in the night. Here a princess masquerades as an orphan boy; a knight of the mind prepares a poison for a treacherous sorceress; and wild men descend from the Mountains of the Moon to ravage the countryside. Against a backdrop of incest and fratricide, alchemy and murder, victory may go to the men and women possessed of the coldest steel...and the coldest hearts. For when kings clash, the whole land trembles.',
	published_date='2000',
	image_url='https://images-na.ssl-images-amazon.com/images/I/91Nl6NuijHL.jpg',isbn='0553579908',
	authors=[grrm],
	genres=[fiction, fantasy],
	shelves=[already_read]
)
db.session.add(book2)

book3 = BookModel(
	title='A Storm of Swords',
	summary='Of the five contenders for power, one is dead, another in disfavor, and still the wars rage as violently as ever, as alliances are made and broken. Joffrey, of House Lannister, sits on the Iron Throne, the uneasy ruler of the land of the Seven Kingdoms. His most bitter rival, Lord Stannis, stands defeated and disgraced, the victim of the jealous sorceress who holds him in her evil thrall. But young Robb, of House Stark, still rules the North from the fortress of Riverrun. Robb plots against his despised Lannister enemies, even as they hold his sister hostage at King’s Landing, the seat of the Iron Throne.',
	published_date='2000',
	isbn='0553106635',
    image_url='https://images-na.ssl-images-amazon.com/images/I/91dlztjGOHL.jpg',
	authors=[grrm],
	genres=[fiction, fantasy],
	shelves=[already_read]
)
db.session.add(book3)

book4 = BookModel(
	title='A Feast for Crows',
	summary='It seems too good to be true. After centuries of bitter strife and fatal treachery, the seven powers dividing the land have decimated one another into an uneasy truce. Or so it appears. . . . With the death of the monstrous King Joffrey, Cersei is ruling as regent in King’s Landing. Robb Stark’s demise has broken the back of the Northern rebels, and his siblings are scattered throughout the kingdom like seeds on barren soil. Few legitimate claims to the once desperately sought Iron Throne still exist—or they are held in hands too weak or too distant to wield them effectively. The war, which raged out of control for so long, has burned itself out.',
	published_date='2006',
	isbn='9780553582024',
    image_url='https://images-na.ssl-images-amazon.com/images/I/81MylCMYnVL.jpg',
	authors=[grrm],
	genres=[fiction, fantasy],
	shelves=[already_read]
)
db.session.add(book4)

book5 = BookModel(
	title='A Dance with Dragons',
	summary='In the aftermath of a colossal battle, the future of the Seven Kingdoms hangs in the balance—beset by newly emerging threats from every direction. In the east, Daenerys Targaryen, the last scion of House Targaryen, rules with her three dragons as queen of a city built on dust and death. But Daenerys has thousands of enemies, and many have set out to find her. As they gather, one young man embarks upon his own quest for the queen, with an entirely different goal in mind.',
	published_date='2013',
	isbn='9780553582017',
    image_url='https://images-na.ssl-images-amazon.com/images/I/81e1rZDeBBL.jpg',
	authors=[grrm],
	genres=[fiction, fantasy],
	shelves=[already_read]
)
db.session.add(book5)

book6 = BookModel(
	title='Touching the Void',
	summary='Joe Simpson and his climbing partner, Simon Yates, had just reached the top of a 21,000-foot peak in the Andes when disaster struck. Simpson plunged off the vertical face of an ice ledge, breaking his leg. In the hours that followed, darkness fell and a blizzard raged as Yates tried to lower his friend to safety. Finally, Yates was forced to cut the rope, moments before he would have been pulled to his own death.',
	published_date='1988',
	isbn='0060730552',
    image_url='https://static.metacritic.com/images/products/movies/8/53b03fab6ead4ac3160e5e633715d94b.jpg',
	authors=[simpson],
	genres=[non_fiction, adventure],
	shelves=[to_read]
)
db.session.add(book6)

book7 = BookModel(
	title='Into the Wild',
	summary='In April 1992 a young man from a well-to-do family hitchhiked to Alaska and walked alone into the wilderness north of Mt. McKinley. His name was Christopher Johnson McCandless. He had given $25,000 in savings to charity, abandoned his car and most of his possessions, burned all the cash in his wallet, and invented a new life for himself. Four months later, his decomposed body was found by a moose hunter.  How McCandless came to die is the unforgettable story of Into the Wild.',
	published_date='1997',
	isbn='0385486804',
    image_url='https://images-na.ssl-images-amazon.com/images/I/811k9HNhaiL.jpg',
	authors=[krakauer],
	genres=[non_fiction, adventure],
	shelves=[to_read]
)
db.session.add(book7)

book8 = BookModel(
	title='Into Thin Air',
	summary='A bank of clouds was assembling on the not-so-distant horizon, but journalist-mountaineer Jon Krakauer, standing on the summit of Mt. Everest, saw nothing that "suggested that a murderous storm was bearing down." He was wrong. The storm, which claimed five lives and left countless more--including Krakauer’s--in guilt-ridden disarray, would also provide the impetus for Into Thin Air, Krakauer’s epic account of the May 1996 disaster.',
	published_date='2013',
	isbn='9780553582017',
    image_url='https://images-na.ssl-images-amazon.com/images/I/81wLeKWJmrL.jpg',
	authors=[krakauer],
	genres=[non_fiction, adventure],
	shelves=[to_read]
)
db.session.add(book8)

book9 = BookModel(
	title='1984',
	summary='Winston Smith toes the Party line, rewriting history to satisfy the demands of the Ministry of Truth. With each lie he writes, Winston grows to hate the Party that seeks power for its own sake and persecutes those who dare to commit thoughtcrimes. But as he starts to think for himself, Winston can’t escape the fact that Big Brother is always watching...',
	published_date='1950',
	isbn='9780451524935',
    image_url='https://images-na.ssl-images-amazon.com/images/I/71-qZ2Z754L.jpg',
	authors=[orwell],
	genres=[fiction, dystopian],
	shelves=[to_read]
)
db.session.add(book9)

book10 = BookModel(
	title='Slaughterhouse-Five',
	summary='Slaughterhouse-Five, an American classic, is one of the world’s great antiwar books. Centering on the infamous firebombing of Dresden, Billy Pilgrim’s odyssey through time reflects the mythic journey of our own fractured lives as we search for meaning in what we fear most.',
	published_date='1969',
	isbn='0812988523',
    image_url='https://images-na.ssl-images-amazon.com/images/I/71QcX1DbklL.jpg',
	authors=[vonnegut],
	genres=[fiction, science_fiction, satire],
	shelves=[to_read]
)
db.session.add(book10)


db.session.commit()
