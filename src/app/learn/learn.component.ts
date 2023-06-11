import { Component } from '@angular/core';
import { PredService } from '../pred.service';

@Component({
  selector: 'app-learn',
  templateUrl: './learn.component.html',
  styleUrls: ['./learn.component.css']
})
export class LearnComponent {
    constructor (private lrn:PredService){}
    learn(age:number,Gender:number,genre:string){
        console.log(age,Gender,genre);
        this.lrn.learn(age,Gender,genre).subscribe(res => console.log(res))
        
    }
}
