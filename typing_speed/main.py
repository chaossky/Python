import time,random

sentences=[
    "Python is amazing.",
    "Typing speed test is fun."
]

text=random.choice(sentences)
print("Type the following sentence as fast as you can:\n")
print(f"✍️{text}\n")
start=time.time()
typed=input("Your Input : ")
end=time.time()
time_taken=end-start
accuracy= sum(a==b for a,b in zip(text,typed))/len(text)
wpm=len(typed.split())/(time_taken/60)
print(f"Time taken : {time_taken:.2f} seconds")
print(f"Accuracy : {accuracy*100:.2f}%")
print(f"WPM : {wpm:.2f} words per minute")