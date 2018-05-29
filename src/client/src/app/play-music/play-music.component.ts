import { Component, OnInit, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-play-music',
  templateUrl: './play-music.component.html',
  styleUrls: ['./play-music.component.css'],
  inputs: ["notes"],
})
export class PlayMusicComponent implements OnInit {

  notes: any;
  convertedNotes = [];

  constructor() { }

  ngOnInit() {
    
  }

  ngOnChanges(changes) {
    if(changes.notes.currentValue) {
      alert(JSON.stringify(this.notes));
      for(let note of this.notes) {
        let array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];        
        for(let one of note) {
          let pitch = one["pitch"];
          let octave = one["octave"];
          array[(octave - 4) * 7 + pitch - 1] = 1;
        }
        this.convertedNotes.push(array);
      }
      alert(JSON.stringify(this.convertedNotes));
    }
  }

  clickImage()  {
  }

}
