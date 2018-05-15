import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MusicSheetComponent } from './music-sheet.component';

describe('MusicSheetComponent', () => {
  let component: MusicSheetComponent;
  let fixture: ComponentFixture<MusicSheetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MusicSheetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MusicSheetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
