girl_group={
 "Classy":
    {
        "member":["Boeun","Hyeju","Hyoungseo","Chawon","Riwon","Sunyoo","Jimin"],
        "Debut_date":"2022.05.05",
        "sosoksa":"M25",
        "songs":["Surprise","Shut Down","classy"]
   },
 
 "IVE":
    {
        "member":["Wongyoung","Yujin","Liz","Rei","Gaeul","Yiseo"],
        "Debut_year":"2021.12.01",
        "sosoksa":"STARSHIP",
        "songs":["Eleven","Love Dive"]
    },
    
"LE SSERAFIM":
    {
        "member":["Chaewon","Sakura","Garam","Eunchae","Kazuha","Yunjin"],
        "Debut_year":"2022.05.02",
        "sosoksa":"soruce Music",
        "songs":["Fearless","Blue Flame"]
    }
}

#print(girl_group)

for key in girl_group:
    print("------------------------------------------")
    print(key)
    
    for member in girl_group[key]:
        print(girl_group[key][member])

