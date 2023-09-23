import random
import time

import funct

#Variable

#--------------- WORD
list_of_word_to_display:list = ['bouilloire', 'discussions', 'intelligent', 'dentifrice', 'microscope', 'japonais', 'cartographie', 'radiation', 'ensorceler', 'taverne', 'cachette', 'chameau', 'flotteur', 'cascade', 'flotteur', 'diligence', 'prononcer', 'vignoble', 'substitution', 'puissance', 'hieroglyphe', 'principal', 'mitrailleuse', 'prisme', 'impulsion', 'violet', 'partenariat', 'digestion', 'photocopie', 'diplomate', 'agitateur', 'himalaya', 'insensible', 'restaurant', 'cosmetique', 'tropique', 'sonnaille', 'muletier', 'bouteille', 'frauduleux', 'armure', 'crasseux', 'obelisque', 'applaudir', 'inspecter', 'marathon', 'sensible', 'commencer', 'visage', 'entacher', 'cicatrice', 'remarques', 'ombre', 'clairon', 'mathematiques', 'ventiler', 'indivisible', 'alarme', 'mouvements', 'martien', 'symphonie', 'lobotomie', 'dauphins', 'objectif', 'gauche', 'droite', 'tromperie', 'quantum', 'condamner', 'abrasif', 'susciter', 'rebelle', 'chaussures', 'trousse', 'princesse', 'glissant', 'nicotine', 'cannelle', 'chemisier', 'melanger', 'chinois', 'horreurs', 'marches', 'humilite', 'tentacule', 'trombone', 'banque', 'carburant', 'annonce', 'viande', 'transport', 'cure-dents', 'avocat', 'couches', 'instruit', 'sondage', 'trolleybus', 'interdimensionnel', 'crocodile', 'holocauste']
#-------
list_loose_expressions:list = ['Gardez la tête haute, demain est un nouveau jour.', 'Chaque défaite est une leçon en soi.', "La victoire n'est qu'un détour sur la route de l'expérience.", "La bonne nouvelle, c'est que vous pouvez maintenant dire que vous êtes un 'expert' en expérience du joueur.", "N'oubliez pas que la plupart des légendes ont un chapitre sur l'échec avant le succès.", "Vous n'avez peut-être pas gagné cette fois-ci, mais c'est le destin de tout super-héros d'avoir une histoire de début un peu cahoteuse.", 'Ne vous inquiétez pas, le bouton "Réessayer" est là pour une raison.', "Vous avez donné le meilleur de vous-même, même si le jeu ne l'a pas remarqué.", 'La victoire est belle, mais la défaite est au moins un excellent professeur de modestie.', 'Vous avez perdu, mais au moins vous avez sauvé virtuellement le monde... en quelque sorte.', "La défaite, c'est comme les légumes : tout le monde doit en avoir un peu.", 'Vous avez perdu, mais au moins vous avez évité une bataille avec un dragon en vrai !', 'Ne vous inquiétez pas, même les experts étaient des débutants une fois... et certains le sont toujours.', 'Vous avez fait de votre mieux, soyez fier/fière de vous.', 'Les défaites forgent le caractère.', 'Continuez à vous améliorer, vous êtes sur la bonne voie.', 'Votre potentiel est illimité, ne baissez pas les bras.']
#-------
list_win_expressions:list = ['Vous avez remporté la victoire !', "C'est une victoire éclatante !", 'Félicitations pour votre triomphe !', 'Vous êtes le maître du jeu !', 'Une victoire bien méritée !', "Gagner n'a jamais été aussi doux !", 'Vous avez montré votre talent !', 'Le titre de champion vous appartient !', 'Excellent travail, vous avez réussi !', 'Vous avez vaincu le dragon du jeu ! Maintenant, où est le dragon réel ?', "Félicitations, vous avez gagné ! Nous vous attendions à l'entraînement des super-héros.", 'Vous êtes un as du jeu ! Puis-je avoir votre autographe ?', "Gagner n'est qu'une des nombreuses choses géniales que vous faites dans la journée.", 'Vous avez gagné ! Les autres joueurs se demandent toujours comment.', 'Vous êtes tellement bon que les robots veulent apprendre de vous.', 'Bravo, vous avez prouvé que les licornes existent - en tout cas dans ce jeu !', 'Vous avez gagné ! Le monde attend désormais votre livre sur les secrets du succès.', 'Vous êtes si bon que même les algorithmes ont besoin de conseils de votre part.', "Gagner n'est qu'une formalité pour vous, non ?"]
#--------------- Hangman

hangman:list = [
      """
+      +---+
+      |   |
+      O   |
+     /|\  |
+     / \  |
+          |
+    =========
    """,
    """
+      +---+
+      |   |
+      O   |
+     /|\  |
+     /    |
+          |
+    =========
    """,
    """
+      +---+
+      |   |
+      O   |
+     /|\  |
+          |
+          |
+    =========
    """,
    """
+      +---+
+      |   |
+      O   |
+     /|   |
+          |
+          |
+   =========
    """,
    """"
+      +---+
+      |   |
+      O   |
+      |   |
+          |
+          |
+    =========
    """,
    """
+      +---+
+      |   |
+      O   |
+          |
+          |
+          |
+    =========
    """,
    """
+      +---+
+      |   |
+          |
+          |
+          |
+          |
+    =========
    """,
        """
+      +---+
+          |
+          |
+          |
+          |
+          |
+    =========
    """,
      """
+           
+          |
+          |
+          |
+          |
+          |
+    =========
    """,
    """
+
+
+
+
+
+
+    =========
    """,

]
#------------------------------------------------------------------------

#-------------- FUNCTION 
def hangman_game(a, b):
    #---------------- GAME USE
    list_of_used_letter:list = []
    point = a
    nbr_game_played = b
    nbr_chance = 9
    mistery_word = list_of_word_to_display[random.randint(0, len(list_of_word_to_display))]
    displayunderscored = "_" * len(mistery_word)
    display = "".join(displayunderscored)
    display_in_game = " ".join(display)

    #--------------- PRINT VARIABLE
    word_contenance = f"--> Your word contain {len(mistery_word)} letters.  "
    gain_a_point = f"-->  Well play you won a point, your new total point is ---> {point}  "
    enter_contain = f"-->  You can enter either a letter or a word with the length of the one you have to guess. Your word contain {len(mistery_word)} letters  "
    already_played = f"-->  You allready played that letter  "
    exit = f"--> You can exit at any moment tiping-->  exit  "
    play_again = "-->  Would you like to play again tap --> 1 "
    stop_playing = "-->  If not tap --> 2  "
    goodbye = f" GOODBYE, SEE YOU SOON "
    #--------------- STYLE
    funct.hangman_name_style()
    time.sleep(2.0)
    funct.printing_style("  Are u ready?  ")
    time.sleep(2.0)
    #----------------------------------------------

    while nbr_chance > 0 and "_" in display:
        funct.hangman_name_style()
        funct.printing_style1(word_contenance,f"--> Total game played {nbr_game_played}  ", f"--> Your total point is {point}.  ", exit)
        print(hangman[nbr_chance], "\n")
        funct.printing_style(f"  {display_in_game}  ")
        letter = input("Letter : ")
        if letter == "exit":
            break
        elif len(letter) == len(mistery_word):
            if letter == mistery_word:
                point += 1
                nbr_game_played += 1
                funct.printing_style(list_win_expressions[random.randint(0, 16)])
                time.sleep(3.0)
                funct.printing_style1(f"--> Total game played {nbr_game_played}  ", f"--> Your total point is {point}.  ", play_again, stop_playing)
                time.sleep(1.0)
                newgame:int = int(input(" Choice --->  "))
                if newgame == 1:
                    hangman_game(point, nbr_game_played)
                else:
                    funct.hangman_name_style()
                    funct.printing_style(goodbye)
                    quit()
            else:
                nbr_chance += -1
                funct.printing_style(f"-->  You got {nbr_chance} chance left. ")
                time.sleep(1.5)
        elif len(letter) > 1 and len(letter) != len(mistery_word):
            funct.printing_style(enter_contain)
            time.sleep(4.0)
            continue
        elif letter in list_of_used_letter:
            funct.printing_style(already_played)
            time.sleep(1.5)
            continue
        elif letter in mistery_word:
            list_of_used_letter.insert(0, letter)
            index = [i for i, c in enumerate(mistery_word) if c == letter]
            for i in index:
                display_in_game = ""
                position:int = i
                display = display[:position] + letter + display[position+1:]
                for i in display:
                    display_in_game += i + " "
            if len(index) > 1:
                found_couple = f"  Well play you found {len(index)} letters  "
                funct.printing_style(found_couple)
                time.sleep(2.0)
                continue
            else:
                found_one = f"  Well play you found {len(index)} letter  "
                funct.printing_style(found_one)
                time.sleep(2.0)
                continue
        elif letter not in mistery_word:
            nbr_chance += -1
            list_of_used_letter.insert(0, letter)
            funct.printing_style(f"-->  You got {nbr_chance} chance left. ")
            time.sleep(1.5)
        else:
            break
    
    if letter == 'exit':
        funct.printing_style("  Heu.... don't you appreciate my game?  ")
        time.sleep(2.0)
        funct.printing_style("  Or maybe it's because you'r bad at this game :)  ")
        time.sleep(2.0)
        funct.printing_style("  Hope to see you soon!  ")
        time.sleep(2.0)
        quit()
    elif "_" not in display and nbr_chance > 0:
        point += 1
        nbr_game_played += 1
        funct.printing_style(list_win_expressions[random.randint(0, len(list_win_expressions))])
        funct.printing_style1(f"--> Total game played {nbr_game_played}  ", f"--> Your total point is {point}.  ", play_again, stop_playing)
        time.sleep(1.0)
        newgame:int = int(input("Choice -->"))
        if newgame == 1:
            hangman_game(point, nbr_game_played)
        else:
            funct.hangman_name_style()
            funct.printing_style(goodbye)
    elif "_" in display or nbr_chance == 0:
        nbr_game_played += 1
        funct.printing_style(list_loose_expressions[random.randint(0, len(list_loose_expressions))])
        time.sleep(3.0)
        funct.printing_style1(f"--> Total game played {nbr_game_played}  ", f"--> Your total point is {point}.  ", play_again, stop_playing)
        time.sleep(2.0)
        newgame:int = int(input("Choice -->"))
        if newgame == 1:
            hangman_game(point, nbr_game_played)
        else:
            funct.hangman_name_style()
            funct.printing_style(goodbye)

hangman_game(0, 0)