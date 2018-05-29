import { Component, OnInit, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-play-music',
  templateUrl: './play-music.component.html',
  styleUrls: ['./play-music.component.css'],
  inputs: ["notes"],
})
export class PlayMusicComponent implements OnInit {

  notes: any;
  start = 0;
  point = 0;
  bank = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  convertedNotes = [];

  constructor() { }

  ngOnInit() {
    
  }

  ngOnChanges(changes) {
    if(changes.notes.currentValue) {
      for(let note of this.notes) {
        let array = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        for(let one of note) {
          let pitch = one["pitch"];
          let octave = one["octave"];
          array[(octave - 4) * 7 + pitch - 1] = 1;
        }
        this.convertedNotes.push(array);
      }
    }
  }

  playSound(wavPoint) {
      for (let i = 0; i < wavPoint.length; i++) {
          if (wavPoint[i] > 0 && this.bank[i] == 0) {
              this.bank[i] = 1;

              var name = i + ".wav";
              var audio = new Audio(name);
              audio.play();
          } else if (wavPoint[i] == 0){
              this.bank[i] = 0;
          }
      }
  }

  playMusic() {
      if (this.point < this.convertedNotes.length && this.start > 0) {
          this.playSound(this.convertedNotes[this.point]);

          this.point++;

          if (this.start > 0)
              setTimeout('playMusic()', 100);
      }
  }

  clickImage()  {
    this.playFun();
  }

  playFun() {
      this.start = 1;
      this.playMusic();
  }
  pauseFun() {
      this.start = 0;
  }
  stopFun() {
      this.start = 0;
      this.point = 0;
  }

}
