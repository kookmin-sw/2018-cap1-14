import { Component, OnInit, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-music-sheet',
  templateUrl: './music-sheet.component.html',
  styleUrls: ['./music-sheet.component.css'],
  inputs:['notes'],
})
export class MusicSheetComponent implements OnInit {
  
  notes: any;
  parts: Array<any> = [];

  constructor() { }

  ngOnInit() {
  }

  ngOnChanges(changes: any) {
    if(changes.notes.currentValue) {
      for(let i = 0; i < Math.floor(this.notes.length / 150); i++) {
        let part = this.notes.slice(i * 150, ((i + 1) * 150) - 1);
        this.parts.push(part);
      }
      let part = this.notes.slice(this.notes.length * 150, this.notes.length * 150 + this.notes.length / 150);
      this.parts.push(part);
    }
  }

}
