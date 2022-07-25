from datetime import datetime

#Date = datetime.date(datetime.now())

def full_seller_name(seller_name):
    seller_name
    full_name = ""
    for word in seller_name:
        full_name =full_name + " " + word
    return full_name

def txt_reader():
    data = []
    with open('C:/Users/kevin/OneDrive/Skrivbord/testfolder/test2.txt', "r", encoding='utf-8') as text_file:
        data = text_file.readlines()
        for x in range(0, len(data)):
            data[x] = data[x][0:-1]
        y, next_first_word = 0, ""
        while y < len(data)-1:
            if data[y].split()[0] == "Total:":
                with open('C:/Users/kevin/OneDrive/Skrivbord/testfolder/test3.txt', "a", encoding='utf-8') as text_file:
                    text_file.write(data[y] + "\n")
                    y += 1
            else:
                y += 1
            first_word = data[y].split()[0]
            if first_word != "Amazon":
                with open('C:/Users/kevin/OneDrive/Skrivbord/testfolder/test3.txt', "a", encoding='utf-8') as text_file:
                    if len(data[y].split()) == 5:
                        text_file.write(data[y].split()[0] + " is seller" + "\n")
                    else:
                        full_name = full_seller_name(data[y].split()[0:-4])
                        text_file.write(full_name + " is seller" + "\n")
                    text_file.write(data[y].split()[-4] + " is amount in stock" + "\n")
                    text_file.write(data[y].split()[-3] + " is price" + "\n")
                    text_file.write(data[y].split()[-2] + " is type" + "\n")
                    text_file.write(data[y].split()[-1] + " is rating" + "\n")
                    if len(data[y+1].split()) < 3:
                        text_file.write(data[y+1] + " is number of reviews" + "\n")
                    if len(data[y+2].split()) == 1:
                        text_file.write(data[y + 2].split()[0] + " is condition" + "\n")
                    else:
                        text_file.write(data[y+2].split()[0] + " is condition" + "\n")
                        text_file.write(data[y + 2].split()[1] + " ")
                        text_file.write(data[y+2].split()[2] + " is arrival date" + "\n")
                    if data[y+3].split()[0] == "Total:":
                        y += 3
                    elif len(data[y+1].split()) > 2:
                        pass
                    else:
                        y += 2
            else:
                with open('C:/Users/kevin/OneDrive/Skrivbord/testfolder/test3.txt', "a", encoding='utf-8') as text_file:
                    text_file.write(data[y].split()[0] + " is seller" + "\n")
                    text_file.write(data[y].split()[1] + " is amount in stock" + "\n")
                    text_file.write(data[y].split()[2] + " is price" + "\n")
                    text_file.write(data[y].split()[3] + " is type" + "\n")
                    text_file.write(data[y].split()[4] + " is condition" + "\n")
                    text_file.write(data[y].split()[5] + " " + data[y].split()[6] + " is arrival date" + "\n")
                    next_first_word = data[y+1].split()[0]
                    if next_first_word == "Total:":
                        y += 1
                    else:
                        pass

txt_reader()
