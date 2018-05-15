import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SheetComponent } from './sheet.component';

describe('SheetComponent', () => {
  let component: SheetComponent;
  let fixture: ComponentFixture<SheetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SheetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SheetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
