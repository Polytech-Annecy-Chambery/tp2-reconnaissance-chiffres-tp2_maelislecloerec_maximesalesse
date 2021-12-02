from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im_bin = image.binarisation(S)
    im_loc = im_bin.localisation()
    sim = 0
    
    for x in range (len(liste_modeles)):
        im_resize = im_loc.resize1(liste_modeles[x].H, liste_modeles[x].W)
        similarité = im_resize.similitude(liste_modeles[x])
        
        if similarité > sim:
            sim = similarité
            nbr_sim = x
        return nbr_sim
        

