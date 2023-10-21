import datetime

from .models import *

# deleting existing data

Club.objects.all().delete()
Stadium.objects.all().delete()
Player.objects.all().delete()
Season.objects.all().delete()
PlayerClubOfSeason.objects.all().delete()
Match.objects.all().delete()
MatchPlayer.objects.all().delete()
MatchAction.objects.all().delete()

# creating object and calling save() method can be changed to 
# create() method (example: Club.objects.create(fields=))

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

inter = Club(club_name="INTER",
    headquarter="Viale della Liberazione 18",
    website="https://www.inter.it/it",
    president="Zhang Kangyang",
    coach="SIMONE INZAGHI",
    assistant_coach="Massimiliano Farris",
    stadium = milan_inter_stadium,
)
    

milan = Club(club_name="MILAN",
    headquarter="Via Aldo Rossi 8, Milano",
    website="https://www.acmilan.com",
    president="Paolo Scaroni",
    coach="STEFANO PIOLI",
    assistant_coach="Giacomo Murelli",
    stadium = milan_inter_stadium,
)


lecce = Club(club_name="LECCE",
    headquarter="Via Colonnello Archimede Costadura, 3, Lecce",
    website="https://www.uslecce.it",
    president="Prof. Avv. Saverio Sticchi Damiani",
    coach="ROBERTO D'AVERSA",
    assistant_coach="Andrea Tarozzi",
    stadium = leece_stadium,
)

inter.save()
milan.save()
lecce.save()

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


season2324 = Season(
    start_date = datetime.date(2023, 8, 19),
    end_date = datetime.date(2024, 2, 1),
)

season2324.save()


# Matches 
lecce_inter_m1 = Match(
    matchday = 1,
    referee = "ROSARIO ABISSO",
    home_team = lecce,
    guest_team = inter,
    home_score = 1,
    guest_score = 2,
    season = season2324,
    date = datetime.date(year=2023, month=9, day=20)
)

milan_lecce_m2 = Match(
    matchday = 2,
    referee = "MATTEO MARCHETTI",
    home_team = milan,
    guest_team = lecce,
    home_score = 0,
    guest_score = 0,
    season = season2324,
    date = datetime.date(year=2023, month=9, day=27)
)

milan_inter_m3 = Match(
    matchday = 3,
    referee = "MATTEO MARCHETTI",
    home_team = milan,
    guest_team = inter,
    home_score = 3,
    guest_score = 2,
    season = season2324,
    date = datetime.date(year=2023, month=10, day=3)
)

lecce_inter_m1.save()
milan_lecce_m2.save()
milan_inter_m3.save()

# Players #

# lecce - inter players
m1_lecce_p1 = MatchPlayer(
    player = lecce_gk,
    match = lecce_inter_m1
)

m1_lecce_p2 = MatchPlayer(
    player = lecce_def,
    match = lecce_inter_m1
)

m1_lecce_p3 = MatchPlayer(
    player = lecce_mid,
    match = lecce_inter_m1
)

m1_lecce_p4 = MatchPlayer(
    player = lecce_sk,
    match = lecce_inter_m1
)

m1_inter_p1 = MatchPlayer(
    player = inter_gk,
    match = lecce_inter_m1
)

m1_inter_p2 = MatchPlayer(
    player = inter_def,
    match = lecce_inter_m1
)

m1_inter_p3 = MatchPlayer(
    player = inter_mid,
    match = lecce_inter_m1
)

m1_inter_p4 = MatchPlayer(
    player = inter_sk,
    match = lecce_inter_m1
)

# 
m2_milan_p1 = MatchPlayer(
    player = milan_gk,
    match = milan_lecce_m2
)

m2_milan_p2 = MatchPlayer(
    player = milan_def,
    match = milan_lecce_m2
)

m2_milan_p3 = MatchPlayer(
    player = milan_mid,
    match = milan_lecce_m2
)

m2_milan_p4 = MatchPlayer(
    player = milan_sk,
    match = milan_lecce_m2
)

m2_lecce_p1 = MatchPlayer(
    player = lecce_gk,
    match = milan_lecce_m2
)

m2_lecce_p2 = MatchPlayer(
    player = lecce_def,
    match = milan_lecce_m2
)

m2_lecce_p3 = MatchPlayer(
    player = lecce_mid,
    match = milan_lecce_m2
)

m2_lecce_p4 = MatchPlayer(
    player = lecce_sk,
    match = milan_lecce_m2
)

m1_lecce_p1.save()
m1_lecce_p2.save()
m1_lecce_p3.save()
m1_lecce_p4.save()

m1_inter_p1.save()
m1_inter_p2.save()
m1_inter_p3.save()
m1_inter_p4.save()

m2_milan_p1.save()
m2_milan_p2.save()
m2_milan_p3.save()
m2_milan_p4.save()

m2_lecce_p1.save()
m2_lecce_p2.save()
m2_lecce_p3.save()
m2_lecce_p4.save()


# MatchAction
m1_g1 = MatchAction(
    match_player = m1_lecce_p3,
    action = 'GOAL',
    minute = 44
)

m1_g2 = MatchAction(
    match_player = m1_inter_p3,
    action = 'GOAL',
    minute = 58
)

m1_g3 = MatchAction(
    match_player = m1_inter_p4,
    action = 'GOAL',
    minute = 71
)

m1_g1.save()
m1_g2.save()
m1_g3.save()


# PalyerClubOfSeason
lecce_p1 = PlayerClubOfSeason(
    player = lecce_gk,
    club = lecce,
    season = season2324,
)

lecce_p2 = PlayerClubOfSeason(
    player = lecce_def,
    club = lecce,
    season = season2324,
)

lecce_p3 = PlayerClubOfSeason(
    player = lecce_mid,
    club = lecce,
    season = season2324,
)

lecce_p4 = PlayerClubOfSeason(
    player = lecce_sk,
    club = lecce,
    season = season2324,
)

inter_p1 = PlayerClubOfSeason(
    player = inter_gk,
    club = inter,
    season = season2324,
)

inter_p2 = PlayerClubOfSeason(
    player = inter_def,
    club = inter,
    season = season2324,
)

inter_p3 = PlayerClubOfSeason(
    player = inter_mid,
    club = inter,
    season = season2324,
)

inter_p4 = PlayerClubOfSeason(
    player = inter_sk,
    club = inter,
    season = season2324,
)

milan_p1 = PlayerClubOfSeason(
    player = milan_gk,
    club = milan,
    season = season2324,
)

milan_p2 = PlayerClubOfSeason(
    player = milan_def,
    club = milan,
    season = season2324,
)

milan_p3 = PlayerClubOfSeason(
    player = milan_mid,
    club = milan,
    season = season2324,
)

milan_p4 = PlayerClubOfSeason(
    player = milan_sk,
    club = milan,
    season = season2324,
)

lecce_p1.save()
lecce_p2.save()
lecce_p3.save()
lecce_p4.save()

inter_p1.save()
inter_p2.save()
inter_p3.save()
inter_p4.save()

milan_p1.save()
milan_p2.save()
milan_p3.save()
milan_p4.save()
