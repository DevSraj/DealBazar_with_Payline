import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinkbankaccountComponent } from './linkbankaccount.component';

describe('LinkbankaccountComponent', () => {
  let component: LinkbankaccountComponent;
  let fixture: ComponentFixture<LinkbankaccountComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LinkbankaccountComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LinkbankaccountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
