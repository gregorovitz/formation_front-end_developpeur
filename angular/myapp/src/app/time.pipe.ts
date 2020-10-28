import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'time'
})
export class TimePipe implements PipeTransform {

  transform(value: number): string { 
    //MM:SS format 
    //const minutes: number = Math.floor(value/60); 
    //return ('00' + minutes).slice(-2) + ':' + ('00' + Math.floor(value - minutes * 60)).slice(-2); 

    // for HH:MM:SS 
    const hours: number = Math.floor(value/(36e5));
    const mins: number = Math.floor((value %36e5)/6e4);
    const secs: number = Math.floor((value %6e4)/1000);
    const milli: number = Math.floor((value%1000))
   
    const minutes: number = Math.floor((value % 3600)/60); 
  return ('00' + hours).slice(-2) + ':' + ('00' + mins).slice(-2) + ':' + ('00' + secs).slice(-2)+':' + ('00' + milli).slice(-3); 
  }

}
