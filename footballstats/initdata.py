import datetime

from .models import *

# creating object and calling save() method can be changed to 
# create() method (example: Club.objects.create(fields=))

inter = Club(club_name="INTER",
    headquarter="Viale della Liberazione 18",
    website="https://www.inter.it/it",
    president="Zhang Kangyang",
    coach="SIMONE INZAGHI",
    assistant_coach="Massimiliano Farris")

milan = Club(club_name="MILAN",
    headquarter="Via Aldo Rossi 8, Milano",
    website="https://www.acmilan.com",
    president="Paolo Scaroni",
    coach="STEFANO PIOLI",
    assistant_coach="Giacomo Murelli")

lecce = Club(club_name="LECCE",
    headquarter="Via Colonnello Archimede Costadura, 3, Lecce",
    website="https://www.uslecce.it",
    president="Prof. Avv. Saverio Sticchi Damiani",
    coach="ROBERTO D'AVERSA",
    assistant_coach="Andrea Tarozzi")

inter.save()
milan.save()
lecce.save()

milan_inter_stadium = Stadium(
    stadium_name = "GIUSEPPE MEAZZA",
    capacity = 75710,
    guest_sector_capacity = None,
    year_of_construction = 1926,
    city = "Milano"
)

leece_stadium = Stadium(
    stadium_name = "ETTORE GIARDINIERO - VIA DEL MARE",
    capacity = 30534,
    guest_sector_capacity = 1075,
    year_of_construction = 1966,
    city = "Lecce"
)

milan_inter_stadium.save()
leece_stadium.save()



inter_gk = Player(
    firstname = "Yann",
    surname = "Sommer",
    role = "goalkeeper",
    date_of_birth = datetime.date(1988, 12, 17),
    nationality = "Swiss"
)

inter_def = Player(
    firstname = "Stefan",
    surname = "De Vrij",
    role = "defender",
    date_of_birth = datetime.date(1992, 2, 5),
    nationality = "Dutch"
)

inter_mid = Player(
    firstname = "Denzel",
    surname = "Dumfries",
    role = "midfielder",
    date_of_birth = datetime.date(1996, 4, 18),
    nationality = "Dutch"
)

inter_sk = Player(
    firstname = "Marko",
    surname = "Arnautovic",
    role = "striker",
    date_of_birth = datetime.date(1989, 4, 19),
    nationality = "Austrian"
)


milan_gk = Player(
    firstname = "Mike",
    surname = "Maignan",
    role = "goalkeeper",
    date_of_birth = datetime.date(1995, 7, 3),
    nationality = "French"
)

milan_def = Player(
    firstname = "Davide",
    surname = "Calabria",
    role = "defender",
    date_of_birth = datetime.date(1996, 12, 6),
    nationality = "Italian"
)

milan_mid = Player(
    firstname = "Yacine",
    surname = "Adli",
    role = "midfielder",
    date_of_birth = datetime.date(2000, 7, 29),
    nationality = "French"
)

milan_sk = Player(
    firstname = "Rafael",
    surname = "Leao",
    role = "striker",
    date_of_birth = datetime.date(1999, 6, 10),
    nationality = "Portuguese"
)


lecce_gk = Player(
    firstname = "Federico",
    surname = "Brancolini",
    role = "goalkeeper",
    date_of_birth = datetime.date(2001, 7, 14),
    nationality = "Italian"
)

lecce_def = Player(
    firstname = "Marin",
    surname = "Pongracic",
    role = "defender",
    date_of_birth = datetime.date(1997, 9, 11),
    nationality = "Croatian"
)

lecce_mid = Player(
    firstname = "Remi",
    surname = "Oudin",
    role = "midfielder",
    date_of_birth = datetime.date(1996, 11, 18),
    nationality = "French"
)

lecce_sk = Player(
    firstname = "Pontus",
    surname = "Almqvist",
    role = "striker",
    date_of_birth = datetime.date(1999, 7, 10),
    nationality = "Sweden"
)

inter_gk.save()

inter_def.save()

inter_mid.save()

inter_sk.save()

milan_gk.save()

milan_def.save()

milan_mid.save()

milan_sk.save()

lecce_gk.save()

lecce_def.save()

lecce_mid.save()

lecce_sk.save()


season2324_p1 = SeasonPart(
    start_date = datetime.date(2023, 8, 19),
    end_date = datetime.date(2024, 2, 1),
    season_part = "1"
)

season2324_p1.save()
