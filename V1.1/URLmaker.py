
with open('Final_List.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

URL = 'https://albiononline2d.com/en/item/id/'

final_list = []
for page in lines:
    final_URL = URL + page
    final_list.append(final_URL)

with open("Final_URLS.txt", "w", encoding='utf-8') as file:
    for item in final_list:
        file.write(item + "\n")
