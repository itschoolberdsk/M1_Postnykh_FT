import hockey_locale as hl
import comp_game_locale as cgl
import normal_dialog_locale as ndl
import key_lines_locale as kll

print(kll.CHOOSE_THEME)

while True:
    choose_theme = input()

    if choose_theme == kll.END_DIALOG:
        print(kll.END_TEXT)
        break
        
    elif hl.HOCKEY in choose_theme:
        print(kll.FIND_OUT_SOMETHING)

        while True:
            thematic_issue = input()

            if thematic_issue == kll.END_DIALOG:
                print(kll.CHOOSE_THEME)
                break

            elif thematic_issue not in hl.HOCKEY_TUPLE:
                print(kll.SUGGESTION)
                continue
                
            print(hl.answerToQuestion.get(thematic_issue))            

    elif cgl.COMP_GAMES in choose_theme:
        print(kll.FIND_OUT_SOMETHING)

        while True:
            thematic_issue = input()

            if thematic_issue == kll.END_DIALOG:
                print(kll.CHOOSE_THEME)
                break

            elif thematic_issue not in cgl.COMP_GAME_TUPLE:
                print(kll.SUGGESTION)
                continue

            print(cgl.answerToQuestion.get(thematic_issue))

    elif ndl.CONVERSATION in choose_theme:
        print(kll.OK_TEXT)

        while True:
            thematic_issue = input()

            if thematic_issue == kll.END_DIALOG:
                print(kll.CHOOSE_THEME)
                break
            
            elif thematic_issue not in ndl.CONVERSATION_TUPLE:
                print(kll.SUGGESTION)
                continue

            print(ndl.answerToQuestion.get(thematic_issue))
