
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from scripts.run_setup import Book


def main():
    engine = create_engine('sqlite:///../data/app.db')
    Session = sessionmaker(bind=engine)

    session = Session()

    book_list = [Book(title='A case of identity', author='Conan Doyle',
                      path="../data/A_Case_Of_Identity-Conan_Doyle.epub"),
                 Book(title='Aladdin', author='Ruth Hobart', path="../data/Aladdin-Ruth_Hobart.epub"),
                 Book(title='Alice in Wonderland', author='Lewis Caroll',
                      path="../data/Alice_in_Wonderland-Lewis_Carroll.epub"),
                 Book(title='Cinderella', author='Ruth Hobart', path="../data/Cinderella-Ruth_Hobart.epub"),
                 Book(title='Lord Arthur Saviles Crime', author='Oscar Wilde',
                      path="../data/Lord_Arthur_Saviles_Crime-Oscar_Wilde.epub"),
                 Book(title='Marley and Me', author='John Grogan', path="../data/Marley_and_Me-John_Grogan.epub"),
                 Book(title='Mr Bean in Town', author='Richard Curtis',
                      path="../data/Mr_Bean_in_Town-Richard_Curtis.epub"),
                 Book(title='One Thousand Dollars', author='O Henry', path="../data/One_Thousand_Dollars-O_Henry.epub"),
                 Book(title='Peter Pan', author='J. M. Barrie', path="../data/Peter_Pan-J_M_Barrie.epub"),
                 Book(title='The Adventure of the Blue Carbuncle', author='Conan Doyle',
                      path="../data/The_Adventure_of_the_Blue_Carbuncle-Conan_Doyle.epub"),
                 Book(title='The Beauty and the Beast', author='Jeanne Marie Leprince De Beaumont',
                      path="../data/The_Beauty_and_the_Beast-Jeanne_Marie_Leprince_De_Beaumont.epub"),
                 Book(title='The Emperors New Clothes', author='Hans Andersen',
                      path="../data/The_Emperors_New_Clothes-Hans_Andersen.epub"),
                 Book(title='The Little Mermaid', author='Hans Andersen',
                      path="../data/The_Little_Mermaid-Hans_Andersen.epub"),
                 Book(title='The Lovely Bones', author='Alice Sebold',
                      path="../data/The_Lovely_Bones-Alice_Sebold.epub"),
                 Book(title='The Man Who Would Be King', author='Rudyard Kipling',
                      path="../data/The_Man_Who_Would_Be_King-Rudyard_Kipling.epub"),
                 Book(title='The Royal Family', author='Cherry Gilchrist',
                      path="../data/The_Royal_Family-Cherry_Gilchrist.epub"),
                 Book(title='The Yellow Face', author='Conan Doyle', path="../data/The_Yellow_Face-Conan_Doyle.epub"),
                 Book(title='Three men in a boat', author='Jerome K. Jerome',
                      path="../data/Three_men_in_a_boat-Jerome_K-Jerome.epub"),
                 Book(title='What Happened at Seacliffe', author='Denise Kirby',
                      path="../data/What_Happened_at_Seacliffe-Denise_Kirby.epub"),
                 Book(title='Zorro', author='Sally M. Stockton', path="../data/Zorro-Sally_M_Stockton.epub")]

    for i in range(20):
        session.add(book_list[i])

    session.commit()


main()