import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-music-sheet-part',
  templateUrl: './music-sheet-part.component.html',
  styleUrls: ['./music-sheet-part.component.css']
})
export class MusicSheetPartComponent implements OnInit {
  @ViewChild("canvas") canvas: ElementRef;
  private canvasContext: CanvasRenderingContext2D;
  currentNote: number;
  notes: any;
  

  constructor() { }
  ngOnInit() {
    this.currentNote = 0;
    this.notes = [{pitch:1, octave:3}, {pitch:1, octave:3}, {pitch:1, octave:4}, {pitch:2, octave:3}, {pitch:3, octave:3}, {pitch:4, octave:3}];
  }

  ngAfterViewInit() {
    const canvasElement: HTMLCanvasElement = this.canvas.nativeElement;
    this.canvasContext = canvasElement.getContext("2d");
    this.canvasContext.lineWidth=3;
    this.canvasContext.beginPath();
    this.canvasContext.moveTo(0, 20 +  10 * 1.8);
    this.canvasContext.lineTo(500, 20 +  10 * 1.8);
    this.canvasContext.moveTo(0, 20 +  20 * 1.8);
    this.canvasContext.lineTo(500, 20 +  20 * 1.8);
    this.canvasContext.moveTo(0, 20 +  30 * 1.8);
    this.canvasContext.lineTo(500, 20 +  30 * 1.8);
    this.canvasContext.moveTo(0, 20 +  40 * 1.8);
    this.canvasContext.lineTo(500, 20 +  40 * 1.8);
    this.canvasContext.moveTo(0, 20 +  50 * 1.8);
    this.canvasContext.lineTo(500, 20 +  50 * 1.8);
    this.canvasContext.stroke(); 
    
    this.canvasContext.lineWidth=10;
    this.canvasContext.strokeStyle = "rgb(100,200,150,1)");
    this.canvasContext.beginPath();
    for(let i = 0; i < this.notes.length; i++) {
      let note = this.notes[i];
      let pitch = 140 - note["pitch"] * 10;
      let octave = (note["octave"] - 3) * 65;
      let start = i * 2;
      let end = start + 2;
      this.canvasContext.moveTo(start, pitch - octave);
      this.canvasContext.lineTo(end, pitch - octave);
    } 
    this.canvasContext.stroke(); 
    

 }

}
