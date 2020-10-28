import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-exo1',
  templateUrl: './exo1.component.html',
  styleUrls: ['./exo1.component.scss']
})
export class Exo1Component implements OnInit {
  nbmillisec:number;
  tmpmillisec:number;
  time:any;
  startTime:number;
  hours:number;
  mins:number;
  secs:number;
  milli:number;
  constructor() { }

  ngOnInit(): void {

    this.nbmillisec=0;
    this.tmpmillisec=0;
    this.hours=0; 
    this.mins=0 ;
    this.secs=0;
    this.milli=0;

  }
  start(){
   this.startTime=Date.now() ;
   this.time=setInterval(()=>{
     this.nbmillisec=this.tmpmillisec+Date.now()+-this.startTime
    this.affichage()
    },1)
  }
  stop(){
    clearInterval(this.time)
    this.tmpmillisec=this.nbmillisec
    this.time=null;
  }
  reset(){
    this.stop()
    this.nbmillisec=0;
    this.tmpmillisec=0;
    this.hours=0; 
    this.mins=0 ;
    this.secs=0;
    this.milli=0;
  }
  affichage(){
    this.hours=Math.floor(this.nbmillisec/(36e5)),
    this.mins=Math.floor((this.nbmillisec %36e5)/6e4),
    this.secs=Math.floor((this.nbmillisec %6e4)/1000);
    this.milli=Math.floor((this.nbmillisec%1000))
    
  }

}
