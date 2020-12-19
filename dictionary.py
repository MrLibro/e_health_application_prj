import text_processing as txt

def creat_dictionary(pubmed):


    abstract = txt.txt_prepration(pubmed.abstract)
    abstract = list(str(abstract).split(" "))
    print(abstract)
    return abstract