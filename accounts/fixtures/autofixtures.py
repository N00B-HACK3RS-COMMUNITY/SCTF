from autofixture import generators, register, AutoFixture
from django.contrib.auth import get_user_model

from accounts.models import UserProfile

user_first_names = [(name, name) for name in (
    'Mahalia',
    'Dalton',
    'Fermina',
    'Isidro',
    'Magdalena',
    'Todd',
    'Olympia ',
    'Beatris',
    'Sina',
    'Luna',
    'Isabelle',
    'Latonya',
    'Santa',
    'Salvatore',
    'Sonia',
    'Carlota',
    'Reginald',
    'Hermila',
    'Chloe',
    'Rick',
    'Cinda',
    'Marietta',
    'Tracey',
    'Ronnie',
    'Sarai',
    'Rosaria',
    'Cordell',
    'Hailey',
    'Sammy',
    'Claude',
    'Elvira',
    'Kayce',
    'Amal',
    'Tessie',
    'Kacie',
    'Sherita',
    'Christene',
    'Reina',
    'Shawana',
    'Colette',
    'Izola',
    'Versie',
    'Eda',
    'Jamal',
    'Marget',
    'Bud',
    'Mae',
    'Newton',
    'Cassandra',
    'Jennine',
    'Garfield',
    'Chante',
    'Maxine',
    'Yoshie',
    'Yolando',
    'Yesenia',
    'Marcelina',
    'Kimi',
    'Margot',
    'Kasie',
    'Herman',
    'Daine',
    'Serina',
    'Nery',
    'Thaddeus',
    'Tricia',
    'Voncile',
    'Geri',
    'Isadora',
    'Carl',
    'Elsy',
    'Boyce',
    'Eryn',
    'Corinne',
    'Carina',
    'Danelle',
    'Bok',
    'Hilario',
    'Bernardina',
    'Jeneva',
    'Russ',
    'Estefana',
    'Ramonita',
    'Rana',
    'Armandina',
    'Kara',
    'Otelia',
    'Eduardo',
    'Leone',
    'Kathey',
    'Sylvester',
    'Eldridge',
    'Justina',
    'Tanisha',
    'Trenton',
    'Mariella',
    'Harrison',
    'Marleen',
    'Moira'
)]


user_last_names = [(name, name) for name in (
    'Leblanc',
    'Kincheloe',
    'Casella',
    'Bregman',
    'Priest',
    'Lape',
    'Broadhead',
    'Ehrhardt',
    'Tarter',
    'Huse',
    'Guyton',
    'Keech',
    'Towns',
    'Wimbley',
    'Gadison',
    'Rubio',
    'Kelleher',
    'Makris',
    'Achorn',
    'Deblasio',
    'Trawick',
    'Hurlbert',
    'Lipsey',
    'Whitby',
    'Fripp',
    'Ohm',
    'Cruickshank',
    'Rahaim',
    'Pace',
    'Hall',
    'Semien',
    'Mattison',
    'Vasko',
    'Backlund',
    'Kincaid',
    'Lundin',
    'Middaugh',
    'Casebolt',
    'Guida',
    'Tugwell',
    'Negri',
    'Tullos',
    'Gallucci',
    'Parmer',
    'Twiford',
    'Agular',
    'Tarkington',
    'Fertig',
    'Elfrink',
    'Kluck',
    'Manner',
    'Matteo',
    'Estell',
    'Pace',
    'Mager',
    'Tucci',
    'Pardee',
    'Hinnenkamp',
    'Wertz',
    'Heck',
    'Keena',
    'Hazeltine',
    'Arnette',
    'Weatherspoon',
    'Reimers ,Mahone',
    'Christine',
    'Cheeseman',
    'Doody',
    'Hasegawa',
    'Leavy',
    'Lepe',
    'Obyrne',
    'Alber',
    'Coil',
    'Galaz',
    'Marcell',
    'Koehn',
    'Markow',
    'Denton',
    'Eldredge',
    'Spillers',
    'Gist',
    'Tokarz',
    'Belcher',
    'Paxton',
    'Minns',
    'Shreffler',
    'Imes',
    'Yuen',
    'Wynne',
    'Janes',
    'Bickett',
    'Plude',
    'Stanberry',
    'Lape',
    'Devenport',
    'Rash',
    'Trainor'
)]

user_usernames = [(name, name) for name in (
    'citrusyfilthy',
    'herbsquit',
    'loanmaniacal',
    'dreamshocked',
    'ocelotpreacher',
    'cornaveron',
    'immodestuphold',
    'smellfungusretrograde',
    'cardiacdeer',
    'sardarlanguid',
    'noodleactin',
    'speedysave',
    'angryhull',
    'gegenscheindiscrete',
    'impalaboars',
    'istanbulfanny',
    'buttiesgenius',
    'pandarannoch',
    'asternrump',
    'jaialaipositron',
    'iguanatopmast',
    'promethiummeet',
    'wellowbyron',
    'paternalcommand',
    'mizunapossible',
    'fireballtugofwar',
    'redheadbathe',
    'shortsusd',
    'cheekyharvey',
    'animalmonktonmead',
    'navigatemalachi',
    'soccerducks',
    'muttletinfatuated',
    'rankedkinloch',
    'sabinepiper',
    'sleddersecret',
    'sputterweyr',
    'abstractwhatever',
    'radonangie',
    'lexifrost',
    'ricoboo',
    'ladderobservance',
    'starsmudge',
    'leukocytebooks',
    'skimjetta',
    'productivevigilant',
    'tarzanlethargic',
    'scopslangley',
    'kentrotating',
    'galileandelectable',
    'driveemily',
    'womenskates',
    'sugarcaneripe',
    'solomonoblateness',
    'canoemortar',
    'emphasizedipper',
    'worthcrispy',
    'combtinted',
    'kenorayogi-bear',
    'talkscolding',
    'riemanncobra',
    'disguisinglattice',
    'pockgnostic',
    'dogheartedgoose',
    'crumpledprint',
    'honeytractor',
    'chungmolecule',
    'tykefemale',
    'jasminefrighten',
    'winghamtogether',
    'deerstubble',
    'slightpeg',
    'hexagonhyena',
    'fleecebrainy',
    'tobermorybrislington',
    'skewexaminer',
    'deliciousgiselle',
    'ticktockwoodland',
    'connemaraentire',
    'ennuiulcers',
    'drudgechirm',
    'granbystruggling',
    'handedenglish',
    'danglyfrowning',
    'elviskietche',
    'cetuspear',
    'bookerpisces',
    'covertraise',
    'walkerrembrandt',
    'thanbiotic',
    'cindersdialysis',
    'gurglelincoln',
    'collagenintrusive',
    'sedatestride',
    'theeayasha',
    'glitcheslydeland',
    'parfaitnicked',
    'timespecific',
    'bottomryunmuzzled',
    'sinupbeat'
)]

class UserAutoFixture(AutoFixture):
    field_values = {
        'username': generators.ChoicesGenerator(choices=user_usernames),
        'first_name': generators.ChoicesGenerator(choices=user_first_names),
        'last_name': generators.ChoicesGenerator(choices=user_last_names),
    }

register(get_user_model(), UserAutoFixture)
register(UserProfile, AutoFixture)

