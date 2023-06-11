import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LearnComponent } from './learn/learn.component';
import { PredictComponent } from './predict/predict.component';

const routes: Routes = [
    {path:"predict",component:PredictComponent},
    {path:"learn",component:LearnComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
