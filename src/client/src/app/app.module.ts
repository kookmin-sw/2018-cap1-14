import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import { LogoComponent } from './logo/logo.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ContentComponent } from './content/content.component';
import { MusicSheetComponent } from './music-sheet/music-sheet.component';
import { MusicSheetPartComponent } from './music-sheet/music-sheet-part/music-sheet-part.component';
import { PlayMusicComponent } from './play-music/play-music.component';

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    LogoComponent,
    SearchBarComponent,
    TopBarComponent,
    ContentComponent,
    MusicSheetComponent,
    MusicSheetPartComponent,
    PlayMusicComponent
  ],
  imports: [
    BrowserModule,
    FormsModule, 
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
