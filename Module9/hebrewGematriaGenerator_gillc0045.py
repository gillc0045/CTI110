# Final Project Phase 1 - Hebrew Gematria Generator
'''A program to read Hebrew characters from input,
 and insure the input is a valid Hebrew character,
 and then generate the corresponding Gematria value'''
# gillc0045
# 7/16


'''main() compares the input with two dictionaries
and prints out the name of the Hebrew character
and the Gematria value of the Hebrew character'''
def main():
    entHebChar = input('Enter a Hebrew letter: ',)
    if entHebChar in hebrewGematriaDict:
        hebrewLetter = hebrewLetterDict.get(entHebChar)
        print ('The character is the Hebrew letter',hebrewLetter)
        gematriaValue = hebrewGematriaDict.get(entHebChar)
        print ('The gematria value of',entHebChar,hebrewLetter,'is',gematriaValue)
    else:
        print ('Incorrect Hebrew character')

hebrewLetterDict = {
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

hebrewGematriaDict = {
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
	
main()
