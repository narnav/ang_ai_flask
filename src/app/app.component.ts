import { Component } from '@angular/core';
import { PredService } from './pred.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'myapp';
  myPred=""
constructor (private prd:PredService){}
predict(age:number, gender:number){
        this.prd.getPredict(age,gender).subscribe(res =>this.myPred=res);
}
}
