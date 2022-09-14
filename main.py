with open("index.html", 'w') as file:
    file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta '
               'http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, '
               'initial-scale=1.0">')
    title_of_page = input("Title :")
    file.write(f'\n\t<title>{title_of_page}</title>\n</head>\n<body>\n')
    count = 1
    while True:
        tag_name = input(f"\nTag {count}:")
        if tag_name == "end" or tag_name == "exit":
            break
        else:
            count += 1
            if tag_name == "ul" or tag_name == "ol":
                file.write(f'<{tag_name}>')
                while True :
                    list_ = input("Lists :")
                    if list_ == "end" or list_ == "exit":
                        break
                    file.write(f'\n<li>{list_}</li>')
                file.write(f'\n</{tag_name}>\n')
            
            elif tag_name == "br" or tag_name == "hr":
                file.write(f'<{tag_name}>\n')
            elif tag_name == "div":
                file.write(f'<{tag_name}>\n')
            elif tag_name == "img":
                src_of_image = input("Enter image source :")
                align_image = input("where to align(left/right/center) :")  
                if align_image == "":         
                    file.write(f'<{tag_name} src="{src_of_image}">\n')
                else :
                    file.write(f'<{tag_name} src="{src_of_image}", align="{align_image}">\n')

            else:   
                tag_class = input("Tag Class Name :")
                tag_id = input("Tag Id Name :")
                inp = input("Inside the tag :") 
                file.write(f'<{tag_name} id="{tag_id}" class="{tag_class}">{inp}</{tag_name}>\n')
    file.write('\n</body>\n</html>')
