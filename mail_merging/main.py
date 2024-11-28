PLACEHOLDER = "[Name]"

with open("mail_merging/Input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    

with open("mail_merging/Input/letters/starting_letter.docx") as letters_file:
    letter_contents = letters_file.read()
    
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
    with open(f"mail_merging/Output/Ready_To_Send/Letter_for_{stripped_name}.docx", "w") as completed_letter:
        completed_letter.write(new_letter)