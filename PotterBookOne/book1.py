# Reads book 1 and breaks it out into seperate txt files based on page

infile = open("../book1.txt", "r") 

content = []
page = []

plist = infile.readline()

while plist :
    if len(page) == 0:
        page.append(plist)
        
    else :
        split_line = plist.split(' ')

        if(split_line[0] != "Page"):
            page.append(plist)

        elif (split_line[0] == "Page"):
            page.append(plist)
            content.append(page)
            page = []

    plist = infile.readline()

infile.close()

ind = 0

for page in content:
    outfile = open("Page" + str(ind) + ".txt", "w")
    trimmed_page = [i for i in page if i != "\n"]

    for line in trimmed_page:
        outfile.write(line)

    outfile.close()
    ind += 1




