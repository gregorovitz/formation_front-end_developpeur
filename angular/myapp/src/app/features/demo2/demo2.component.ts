import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-demo2',
  templateUrl: './demo2.component.html',
  styleUrls: ['./demo2.component.scss']
})
export class Demo2Component implements OnInit {
  compt:number;

  constructor() { }

  ngOnInit(): void {
    this.compt=0;
  }
  increase(){
    this.compt++;
  }
  decrease(){
    this.compt--;
  }
  test(){
    return this.compt==0 || this.compt==9
  }
}
