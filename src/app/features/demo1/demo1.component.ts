import { Component, OnInit } from '@angular/core';
import { Console } from 'console';

@Component({
  selector: 'app-demo1',
  templateUrl: './demo1.component.html',
  //template: "<p>Hello</p>",
  styleUrls: ['./demo1.component.scss']
})
export class Demo1Component implements OnInit {

  someString: string;

  someNumber: number;

  someDate: Date;

  someBoolean: boolean;

  someVariable: any;

  constructor() { }

  ngOnInit(): void {

    this.someString = 'AnGUlar';
    this.someNumber = 42.4561122;
    this.someDate = new Date();
    this.someBoolean = true;
    this.someVariable = 'World';

    setTimeout(() => {
      this.someVariable = 'Hello World !!!'
    }, 2000);
  }

}
