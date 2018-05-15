import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-music-sheet-part',
  templateUrl: './music-sheet-part.component.html',
  styleUrls: ['./music-sheet-part.component.css']
})
export class MusicSheetPartComponent implements OnInit {
  private cx: CanvasRenderingContext2D;

  @ViewChild("canvas") canvas: ElementRef;
  

  constructor() { }
  ngOnInit() {
   
  }
  ngAfterViewInit() {
    const canvasEl: HTMLCanvasElement = this.canvas.nativeElement;
    this.cx = canvasEl.getContext("2d");
    this.cx.lineWidth=3;
    this.cx.beginPath();
    this.cx.moveTo(0, 10 * 2.5);
    this.cx.lineTo(500, 10 * 2.5);
    this.cx.moveTo(0, 20 * 2.5);
    this.cx.lineTo(500, 20 * 2.5);
    this.cx.moveTo(0, 30 * 2.5);
    this.cx.lineTo(500, 30 * 2.5);
    this.cx.moveTo(0, 40 * 2.5);
    this.cx.lineTo(500, 40 * 2.5);
    this.cx.moveTo(0, 50 * 2.5);
    this.cx.lineTo(500, 50 * 2.5);
    this.cx.stroke(); 
 }

}
