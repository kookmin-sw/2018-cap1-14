import { Component, OnInit, AfterViewInit, ViewChild, ElementRef, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-music-sheet-part',
  templateUrl: './music-sheet-part.component.html',
  styleUrls: ['./music-sheet-part.component.css'],
  inputs: ['part', ],
})
export class MusicSheetPartComponent implements OnInit {
  @ViewChild("canvas") canvas: ElementRef;
  private canvasContext: CanvasRenderingContext2D;
  currentNote: number;
  notes: any;
  part: any;
  testNotes = [[{pitch:5, octave:4}], [{pitch:5, octave:4}], [{pitch:5, octave:4}], [{pitch:4, octave:4}], [{pitch:3, octave:4}], [{pitch:2, octave:4}], [{pitch:1, octave:4}], [{pitch:1, octave:5}], [{pitch:2, octave:5}]];
  

  constructor() { }
  ngOnInit() {
    this.currentNote = 0; 
  }

  drawSheet() {
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
    let context = this.canvasContext; 
    let clefImage = new Image();
    clefImage.onload = function() {
      context.drawImage(clefImage, 0, 10, 10, 130);
    };
    clefImage.src = "https://i.pinimg.com/originals/b3/3d/cd/b33dcd63310419d58a84067db0d8f0f1.png"
    
    this.canvasContext.lineWidth=10;
    this.canvasContext.strokeStyle = "rgb(100,200,150,1)";
    this.canvasContext.beginPath();
    for(let i = 0; i < this.notes.length; i++) {
      for(let note of this.notes[i]) {
        let pitch = 141 - note["pitch"] * 10;
        let octave = (note["octave"] - 4) * 55;
        let start = i * 2 + 25;
        let end = start + 2;
        this.canvasContext.moveTo(start, pitch - octave);
        this.canvasContext.lineTo(end, pitch - octave);
      }
    } 
    this.canvasContext.stroke(); 
  }
  ngOnChanges(changes) {
    if(changes.part.currentValue) {
      this.notes = this.part;
      //this.notes = this.testNotes;
      this.drawSheet();     
    }
  }

}
