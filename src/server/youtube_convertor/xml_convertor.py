

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
                            '<divisions>4</divisions>\n' +
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
        
        m_number = 1
        duration = 0
        all_duration = 0
        beam = 0
        
        starting = True
        
        before_duration = 0
        before_note = "_"
        for note in notes:
            #duration check
            if (before_note == note):
                all_duration += 1
                duration += 1
            else:
                if starting:
                    starting = False
                else:
                    if len(before_note) > 1:
                        steb = before_note[0]
                        octave = before_note[1]
                        note_xml = ('<note>\n' +
                                        '<pitch>\n' +
                                            '<step>' + steb + '</step>\n' +
                                            '<octave>' + str(int(octave) + 1) + '</octave>\n' +
                                        '</pitch>\n' +
                                        '<duration>' + str(duration) + '</duration>\n' +
                                        '<type>whole</type>\n')
                        
                        note_xml_beam = ""
                        if (duration == before_duration) and (duration > 0):
                            if duration < 3
                                if beam == 0:
                                    note_xml_beam += ('<beam number="1">begin</beam>')
                                    if duration < 2:
                                        note_xml_beam += ('<beam number="2">begin</beam>')
                                else:
                                    note_xml_beam += ('<beam number="1">continue</beam>')
                                    if duration < 2:
                                        note_xml_beam += ('<beam number="2">continue</beam>')
                                beam += 1
                        elif duration > 0:
                            if (duration < 3) and (beam > 0):
                                note_xml_beam += ('<beam number="1">end</beam>')
                                if duration < 2:
                                    note_xml_beam += ('<beam number="2">end</beam>')
                                beam = 0
                            before_duration = duration

                        note_xml_end = ('</note>\n')
                        
                        note_xml += note_xml_beam
                        note_xml += note_xml_end
                        
                        if all_duration > 16:
                            all_duration = 1
                            m_number += 1
                
                            new_measure = ('</measure>\n' + 
                                           '<measure number="' + str(m_number) + '">\n')
                            note_xml += new_measure

                        notes_xml += note_xml
                
                before_note = note
                duration = 1
                
        if len(before_note) > 1:
            steb = before_note[0]
            octave = before_note[1]
            note_xml = ('<note>\n' +
                            '<pitch>\n' +
                                '<step>' + steb + '</step>\n' +
                                '<octave>' + str(int(octave) + 1) + '</octave>\n' +
                            '</pitch>\n' +
                            '<duration>' + str(duration) + '</duration>\n' +
                            '<type>whole</type>\n')

            note_xml_beam = ""
            if (duration == before_duration) and (duration > 0):
                if duration < 3
                    if beam == 0:
                        note_xml_beam += ('<beam number="1">begin</beam>')
                        if duration < 2:
                            note_xml_beam += ('<beam number="2">begin</beam>')
                    else:
                        note_xml_beam += ('<beam number="1">continue</beam>')
                        if duration < 2:
                            note_xml_beam += ('<beam number="2">continue</beam>')
                    beam += 1
            elif duration > 0:
                if (duration < 3) and (beam > 0):
                    note_xml_beam += ('<beam number="1">end</beam>')
                    if duration < 2:
                        note_xml_beam += ('<beam number="2">end</beam>')
                    beam = 0
                before_duration = duration

            note_xml_end = ('</note>\n')

            note_xml += note_xml_beam
            note_xml += note_xml_end

            if all_duration > 16:
                all_duration = 1
                m_number += 1

                new_measure = ('</measure>\n' + 
                               '<measure number="' + str(m_number) + '">\n')
                note_xml += new_measure

            notes_xml += note_xml
            
        print(header + notes_xml + footer)
        
        return header + notes_xml + footer
                
                    
