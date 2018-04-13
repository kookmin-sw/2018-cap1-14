

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
        header = ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + 
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
                          '</attributes>\n')
  
        footer = ('</measure>\n' + 
                '</part>\n' + 
              '</score-partwise>"')

        notes_xml = ""
        duration = 1
        for note in notes:
            if len(note) == 1:
                duration += 1
            else:
                steb = note[0]
                octave = note[1]
                note_xml = ('<note>\n' +
                                '<pitch>\n' +
                                    '<step>' + str(steb) + '</step>\n' +
                                    '<octave>' + str(octave) + '</octave>\n' +
                                '</pitch>\n' +
                                '<duration>' + str(duration) + '</duration>\n' +
                                '<type>whole</type>\n' +
                            '</note>\n')
                duration = 1
            notes_xml += note_xml
            
        return header + notes_xml + footer
                
                    
