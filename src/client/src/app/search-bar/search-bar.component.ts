import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css'],
})
export class SearchBarComponent implements OnInit {

  youtubeUrl: string;

  constructor(public http: HttpClient) { 
    this.youtubeUrl="";
  }

  ngOnInit() {
  }

  onSubmit() {
    let serverUrl = "http://localhost:5000/extract";
    this.http.post(serverUrl, {youtubeUrl: this.youtubeUrl}).subscribe(data => {
        alert("test");
    }, err=> {
        alert("err");
    });
  }

}
