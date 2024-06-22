dict01={"Kimyoungmyung":1000,
        "Yoonseokhyun":1500,
        "Jooyeolmae":1700,
        "Jangbonghwan":3000,
        "Kimsoyoung":4000}

print("Auction Winner", max(dict01, key=dict01.get))

