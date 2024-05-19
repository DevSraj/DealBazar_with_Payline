import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InstantloanComponent } from './instantloan.component';

describe('InstantloanComponent', () => {
  let component: InstantloanComponent;
  let fixture: ComponentFixture<InstantloanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [InstantloanComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InstantloanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
