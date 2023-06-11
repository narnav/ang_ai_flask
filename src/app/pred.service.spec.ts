import { TestBed } from '@angular/core/testing';

import { PredService } from './pred.service';

describe('PredService', () => {
  let service: PredService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PredService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
