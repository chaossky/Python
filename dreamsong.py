dreams_and_challenges_songs = [
    (1, "Rise Again", "A song about standing back up after every fall, refusing to be defeated by setbacks. It’s about believing in yourself, embracing the struggle, and knowing that every failure is just another step toward success."),
    (2, "Unstoppable Now", "A song about finally finding the courage to chase your dreams fearlessly. It’s about breaking free from doubt, ignoring the naysayers, and running toward your goals with unstoppable energy."),
    (3, "Beyond The Horizon", "A song about looking past the limits placed on you, knowing there’s something greater waiting. It’s about pushing boundaries, dreaming bigger, and daring to see beyond what others believe is possible."),
    (4, "No Limits", "A song about breaking through walls and proving that nothing can hold you back. It’s about silencing fear, stepping outside your comfort zone, and realizing that you are capable of more than you ever imagined."),
    (5, "Chasing The Stars", "A song about reaching for the impossible, refusing to settle for anything less than your biggest dreams. It’s about believing that even the highest goals are within reach if you never stop chasing them."),
    (6, "Brave Enough", "A song about overcoming fear and daring to take the first step toward your dreams. It’s about trusting yourself, embracing uncertainty, and understanding that courage isn’t the absence of fear but moving forward despite it."),
    (7, "The Next Chapter", "A song about starting fresh and writing a new story for yourself. It’s about leaving behind old doubts, stepping into the unknown, and creating a future filled with endless possibilities."),
    (8, "Never Back Down", "A song about standing your ground and refusing to quit, no matter how tough things get. It’s about resilience, determination, and proving to yourself that you have the strength to keep going."),
    (9, "Run With Fire", "A song about chasing your dreams with passion and intensity. It’s about running toward your goals without hesitation, fueled by ambition and the desire to make every moment count."),
    (10, "Dreamer’s Road", "A song about walking the path of dreams, even when it’s uncertain and difficult. It’s about trusting the journey, learning from every challenge, and knowing that each step forward brings you closer to your dreams."),
    (11, "Fearless Heart", "A song about having the courage to stand tall against the odds. It’s about facing challenges head-on, believing in yourself, and refusing to let fear dictate your path."),
    (12, "Keep Believing", "A song about holding on to faith even when things seem impossible. It’s about pushing through self-doubt, embracing failures as lessons, and never losing sight of the dream that fuels you."),
    (13, "Dare To Fly", "A song about taking risks and trusting that you have what it takes to soar. It’s about letting go of fear, spreading your wings, and embracing the adventure of chasing your dreams."),
    (14, "Make It Happen", "A song about turning dreams into reality through hard work and determination. It’s about putting in the effort, staying committed, and proving to yourself that anything is possible."),
    (15, "Stronger Than Yesterday", "A song about growing through challenges and coming out stronger on the other side. It’s about using struggles as stepping stones, learning from mistakes, and realizing your own strength."),
    (16, "Path To Glory", "A song about the long and winding journey toward success. It’s about persistence, overcoming obstacles, and staying focused on your goals even when the road gets tough."),
    (17, "Rewrite The Stars", "A song about taking control of your own destiny and refusing to let fate decide for you. It’s about defying expectations, challenging limits, and creating your own future."),
    (18, "Turn The Page", "A song about moving forward and not letting the past define you. It’s about embracing change, learning from experience, and stepping boldly into a new chapter of your life."),
    (19, "No Looking Back", "A song about letting go of regrets and focusing on what’s ahead. It’s about choosing to move forward, believing in yourself, and never letting the past hold you back."),
    (20, "One More Step", "A song about taking things one step at a time, knowing that progress is made through persistence. It’s about celebrating small victories, staying patient, and trusting that every step brings you closer to your dreams.")
]

# 데이터프레임 생성
df_dreams = pd.DataFrame(dreams_and_challenges_songs, columns=["No", "Title", "Description"])

# 엑셀 파일로 저장
dreams_excel_path = "../dreams_and_challenges_songs.xlsx"
df_dreams.to_excel(dreams_excel_path, index=False, encoding="utf-8")

dreams_excel_path