import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.scss']
})
export class ContentComponent implements OnInit {
  
  notes: string;  

  constructor() { }

  ngOnInit() {
  }

  getNote(notes: string) {
    this.notes = notes;
  }
}
