import { Component } from '@angular/core';
import { PredService } from '../pred.service';
@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent {
    title = 'myapp';
    myPred=""
  constructor (private prd:PredService){}
  predict(age:number, gender:number){
          this.prd.getPredict(age,gender).subscribe(res =>this.myPred=res);
  }
}
