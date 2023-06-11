import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class PredService {
    SERVER_URL = "http://127.0.0.1:5000/"
    constructor(private prd: HttpClient) { }

    getPredict(age: number, gender: number): Observable<any> {
        console.log({ age, gender });
        return this.prd.post<any>(this.SERVER_URL+"pred", { age, gender });
    }

    learn(age: number, gender: number,genre:string): Observable<any> {
        console.log({ age, gender });
        return this.prd.post<any>(this.SERVER_URL+"learn", { age, gender,genre });
    }
}
