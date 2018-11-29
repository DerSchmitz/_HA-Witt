#Run-instruction: python C:\Users\developer\_HA-Witt\Bundestag.py
import re
import codecs
import os
# Create relative path to directory
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Bundestagsabgeordnete.txt')

# Open File
with codecs.open(filename, 'r', encoding='utf-8') as fbt:
    # read line for line
      bundestag = fbt.readlines()

      # Iterate lines
      for line in bundestag:

        # clean lines of information without purppose for the email_Adress

        ## clean every additional information in brackets
        ersatzLine = re.sub(" \(.*\)", "", line)
        ## clean every title or abbreviation Prof. , Dr., A., h. etc.
        ersatzLine = re.sub(" [A-Za-z]*\.", "", ersatzLine)
        ## clean line breaks
        ersatzLine = re.sub("\n", "", ersatzLine)

        # clean all Umlaute
        ersatzLine = re.sub("[äÄ]", "ae", ersatzLine)
        ersatzLine = re.sub("[öÖ]", "oe", ersatzLine)
        ersatzLine = re.sub("[üÜ]", "ue", ersatzLine)
        ersatzLine = re.sub("ß", "ss", ersatzLine)
        ersatzLine = re.sub("[éÉ]", "e", ersatzLine)

        # nachname = re.sub("([a-zA-ZäöüÄÖÜß])\w+", ersatzLine)
        #parse second Name
        nachname = re.sub(",.*", "",ersatzLine)
        nachname = re.sub(" ", "",nachname)
        nachname = re.sub("\?", "",nachname)

        # parse first name
        vorname = re.sub(".*, ", "",ersatzLine)
        vorname = re.sub(" \|.*", "",vorname)
        vorname = re.sub(" .*", "",vorname)

        # build Emails-Adresses
        emailAdress = vorname + "." + nachname + "@bundestag.de"

        # Add EMails Adress to its line
        finalLine =   re.sub(".\n", " * "+emailAdress , line);

        # Print Line
        print(nachname)

fbt.close();
