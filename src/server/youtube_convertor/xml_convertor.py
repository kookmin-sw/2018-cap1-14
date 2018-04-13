

class XmlConvertor(object):

    def convert(notes):
        '''
        covert note array to Music xml
        parameters -
            notes : list<string>
                array of note, ex({"C3", "D3", "E3", "F3", "G3", "A3", "B3"})
        returns -
            xml : str
                xml string typed by music xml 
        '''
        for note in notes:
            #TODO
            pass
        #test code 
        xml = ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + 
               '<!DOCTYPE score-partwise PUBLIC\n' +
                    '"-//Recordare//DTD MusicXML 3.0 Partwise//EN"\n' +
                    '"http://www.musicxml.org/dtds/partwise.dtd">\n' +
                '<score-partwise version="3.0">\n' +
                  '<part-list>\n' +
                    '<score-part id="P1">\n' +
                      '<part-name>Music</part-name>\n' +
                    '</score-part>\n' +
                  '</part-list>\n' +
                  '<part id="P1">\n' +
                    '<measure number="1">\n' +
                      '<attributes>\n' +
                        '<divisions>1</divisions>\n' +
                        '<key>\n' +
                          '<fifths>0</fifths>\n' +
                        '</key>\n' +
                        '<time>\n' +
                          '<beats>4</beats>\n' +
                          '<beat-type>4</beat-type>\n' +
                        '</time>\n' +
                        '<clef>\n' +
                          '<sign>G</sign>\n' +
                          '<line>2</line>\n' +
                        '</clef>\n' +
                      '</attributes>\n' +
                      '<note>\n' +
                        '<pitch>\n' +
                          '<step>C</step>\n' +
                          '<octave>4</octave>\n' +
                        '</pitch>\n' +
                        '<duration>4</duration>\n' +
                        '<type>whole</type>\n' +
                      '</note>\n' +
                    '</measure>\n' + 
                  '</part>\n' + 
                '</score-partwise>"')
        #test code
        return xml
                
                    
