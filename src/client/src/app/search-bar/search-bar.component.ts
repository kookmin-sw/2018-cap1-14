import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { OSMD } from "opensheetmusicdisplay";

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css'],
})
export class SearchBarComponent implements OnInit {

  youtubeUrl: string;
  @Output() getNoteEmitter:EventEmitter<string> = new EventEmitter<string>();
  headers;
  constructor(public http: HttpClient) { 
    this.youtubeUrl="";
    this.headers = new HttpHeaders({
      'Content-Type':  'application/json',
    })
  }

  ngOnInit() {
  }

  onSubmit() {
    let serverUrl = "http://localhost:5000/extract";
    this.http.post(serverUrl, {"youtubeUrl":this.youtubeUrl}, this.headers).subscribe((data) => {
      this.getNoteEmitter.emit(data["notes"]);
      //this.openSheet(data["xml"]);
    });
  }

  openSheet(xml) {
    let openSheetMusicDisplay = new OSMD("sheet-test");
    openSheetMusicDisplay
      .load(xml)
      .then(
        () => {
          openSheetMusicDisplay.render();
        }, (err) => {
          alert(err);
        }
      );
  }

}
