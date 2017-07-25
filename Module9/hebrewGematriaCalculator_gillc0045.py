# CTI 110 - Final Project - Hebrew Gematria Calculator
'''A program to read Hebrew strings from input,
 and then sum the Gematria values of the letters'''
# gillc0045
# 7/16
	
def main():
    # The first two test strings are words and the last is a phrase.
    # testStrHeb1 = 'שלום'
    # testStrHeb2 = 'יהושע'
    # testStrHeb3 = 'אלוהיםשמיםוארץ'
    hebString = input ('\n Input a Hebrew word or phrase: ',)

    # Explanation of the program's function
    print ('\n* This program will accept Hebrew words and phrases for *')
    print ('* the purpose of calculating the Gematria value of each *')
    print ('* letter and calculating the Gematria sum of the script *\n')

    # Explanation of the table output
    print ('','#######    Legend of Hebrew Gematria Table  #######')
    print ('','#','Col-1: Gematria values of the Hebrew script')
    print ('','#','Col-2: Hebrew characters of the script entered')
    print ('','#','Col-3: Letter names of the Hebrew characters')
    print ('','# ----------------------------------------------- #')
    print ('','#','Hebrew reads from right to left. The 1st letter')
    print ('','#','of Hebrew script is on the far right of a word ')
    print ('','#','or phrase. Beginning with the 1st letter of the')
    print ('','#','script-inputted, each row in the Gematria Table')
    print ('','#','lists each value of the letters in the script.')
    print ('','# ----------------------------------------------- #')
    print ('','#','The last row is the sum of the Gematria values,')
    print ('','#','which is also the Gematria value of the script.')
    print ('','# _______________________________________________ #')
    print ('','#                                                 #')
    
    # Simple formatting of table output
    print ('','#######         Hebrew Gematria Table       #######')
    print ('','# ----------------------------------------------- #')
    print ('','# Col-1','\t','Col-2','\t','\t','Col-3')
    print ('','# ----------------------------------------------- #')
    scriptGem = 0
    for hebScript in hebString:
        scriptVal = Hebrew_Value_Dict.get(hebScript)
        scriptLet = Hebrew_Letter_Dict.get(hebScript)
        scriptGem += int(scriptVal)
        print (' #',scriptVal,'\t','=','\t',hebScript,'\t','=','\t',scriptLet)
    print ('','# ----------------------------------------------- #')
    print (' #',scriptGem,'= Gematria value of ==',hebString)
    print ('','# _______________________________________________ #')
    
Hebrew_Value_Dict = {
    "א" : 1,
    "ב" : 2,
    "ג" : 3,
    "ד" : 4,
    "ה" : 5,
    "ו" : 6,
    "ז" : 7,
    "ח" : 8,
    "ט" : 9,
    "י" : 10,
    "ך" : 500,
    "כ" : 20,
    "ל" : 30,
    "ם" : 600,
    "מ" : 40,
    "ן" : 700,
    "נ" : 50,
    "ס" : 60,
    "ע" : 70,
    "ף" : 800,
    "פ" : 80,
    "ץ" : 900,
    "צ" : 90,
    "ק" : 100,
    "ר" : 200,
    "ש" : 300,
    "ת" : 400}

Hebrew_Letter_Dict = {
    "א" : 'ALEPH',
    "ב" : 'BETH',
    "ג" : 'GIMMEL',
    "ד" : 'DALET',
    "ה" : 'HE',
    "ו" : 'VAV',
    "ז" : 'ZAYIN',
    "ח" : 'CHET',
    "ט" : 'TES',
    "י" : 'YOD',
    "ך" : 'FINAL KAPH',
    "כ" : 'KAPH',
    "ל" : 'LAMED',
    "ם" : 'FINAL MEM',
    "מ" : 'MEM',
    "ן" : 'FINAL NUN',
    "נ" : 'NUN',
    "ס" : 'SAMECH',
    "ע" : 'AYIN',
    "ף" : 'FINAL PE',
    "פ" : 'PE',
    "ץ" : 'FINAL TZADDI',
    "צ" : 'TZADDI',
    "ק" : 'QUF',
    "ר" : 'RESH',
    "ש" : 'SCHIN',
    "ת" : 'TAU'}

main()

