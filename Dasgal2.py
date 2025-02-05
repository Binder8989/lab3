lesson_1 = "Программ хангамжийн бүтээлт"
lesson_2 = "Программчлалын үндэс"

print(f"Хичээл 1-ийн нэр: {lesson_1}")
print(f"Хичээл 2-ийн нэр: {lesson_2}\n")

index = int(input("Хичээл 1-ийн нэрэнд Хичээл 2-ын ямар дугаарт байгаа үгийг хайх вэ?: "))

word_to_search = lesson_2.split()[index]  
position = lesson_1.find(word_to_search)  

print(f"{index} дугаар дахь \"{word_to_search}\" үсэг хичээл 1-ийн нэрэнд {position} дугаарт дээр олдлоо.")