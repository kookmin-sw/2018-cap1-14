import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MusicSheetPartComponent } from './music-sheet-part.component';

describe('MusicSheetPartComponent', () => {
  let component: MusicSheetPartComponent;
  let fixture: ComponentFixture<MusicSheetPartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MusicSheetPartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MusicSheetPartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
