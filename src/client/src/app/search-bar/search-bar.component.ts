import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css'],
})
export class SearchBarComponent implements OnInit {

  youtubeUrl: string;
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
        alert(JSON.stringify(data));
    });
  }

}
