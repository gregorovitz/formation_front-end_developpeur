import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-exo1',
  templateUrl: './exo1.component.html',
  styleUrls: ['./exo1.component.scss']
})
export class Exo1Component implements OnInit {


  compt: number;

  id: any;

  memory : number;

  constructor() { }

  ngOnInit(): void {
    this.compt = 0;
    this.memory = 0;
  }

  start() {
    let startTime = Date.now();
    this.id = setInterval(() => {
      this.compt = Date.now() - startTime + this.memory;
    }, 1);
  }

  stop() {
    clearInterval(this.id);
    this.memory = this.compt;
    this.id = null;
  }

  reset() {
    this.stop();
    this.compt = 0;
    this.memory = 0;
  }

}
