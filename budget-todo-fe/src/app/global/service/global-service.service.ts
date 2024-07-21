import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GlobalServiceService {

  constructor(private _http: HttpClient) { }

  getCardDetails() {
    return this._http.get('http://127.0.0.1:8000/creditcards/cards');
  }
}
