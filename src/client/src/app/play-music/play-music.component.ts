import { Component, OnInit, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-play-music',
  templateUrl: './play-music.component.html',
  styleUrls: ['./play-music.component.css'],
  inputs: ["notes"],
})
export class PlayMusicComponent implements OnInit {

  notes: any;

  constructor() { }

  ngOnInit() {
    
  }

  ngOnChanges(changes) {
    if(changes.notes.currentValue) {
      alert(JSON.stringify(this.notes));
    }
  }

  clickImage()  {
    
  }

}
